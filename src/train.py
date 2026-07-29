"""Train the pinned CariSurg emergency-department triage model.

Run from the repository root:

    python scripts/train.py --config config.yaml
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any

import yaml
from sklearn.model_selection import train_test_split

# Make repository-root imports work when this file is run directly.
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.data import clean_data, load_data
from src.features import select_final_features
from src.model import build_model, train_model, evaluate_model, save_model


def parse_args() -> argparse.Namespace:
    """Read command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Train and evaluate the pinned CariSurg triage model."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("config.yaml"),
        help="Path to the YAML configuration file.",
    )
    return parser.parse_args()


def load_config(config_path: Path) -> dict[str, Any]:
    """Load and validate the YAML configuration."""
    if not config_path.exists():
        raise FileNotFoundError(
            f"Config file not found: {config_path}. "
            "Run this command from the repository root."
        )

    with config_path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    if not isinstance(config, dict):
        raise ValueError("The config file must contain a YAML mapping.")

    required_sections = {"data", "model", "training", "outputs"}
    missing_sections = required_sections.difference(config)

    if missing_sections:
        raise KeyError(
            "Config is missing required section(s): "
            + ", ".join(sorted(missing_sections))
        )

    return config


def resolve_repo_path(path_value: str | Path) -> Path:
    """Resolve a config path relative to the repository root."""
    path = Path(path_value)
    return path if path.is_absolute() else REPO_ROOT / path


def save_metrics(metrics: dict[str, Any], output_path: Path) -> None:
    """Save evaluation metrics as JSON."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    serialisable_metrics = {
        key: value.item() if hasattr(value, "item") else value
        for key, value in metrics.items()
    }

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(serialisable_metrics, file, indent=2)


def main() -> None:
    """Run the complete training pipeline."""
    args = parse_args()
    config = load_config(resolve_repo_path(args.config))

    data_path = resolve_repo_path(config["data"]["raw_path"])
    model_path = resolve_repo_path(config["outputs"]["model_path"])
    metrics_path = resolve_repo_path(config["outputs"]["metrics_path"])

    print("=" * 68)
    print("CariSurg ED Triage — Training Pipeline")
    print("=" * 68)
    print(f"Config: {resolve_repo_path(args.config)}")
    print(f"Data:   {data_path}")

    # 1. Load and clean the raw dataset.
    raw_df = load_data(data_path)
    clean_df = clean_data(
        raw_df,
        target=config["data"].get("target", "esi"),
    )

    print(f"Raw dataset shape:     {raw_df.shape}")
    print(f"Clean dataset shape:   {clean_df.shape}")

    # 2. Reproduce the final Week 7 feature set:
    #    original eligible triage-time features + age,
    #    excluding MAP and engineered features.
    X, y = select_final_features(
        clean_df,
        target=config["data"].get("target", "esi"),
        include_age=config["data"].get("include_age", True),
    )

    expected_feature_count = config["data"].get("expected_feature_count")
    if (
        expected_feature_count is not None
        and X.shape[1] != int(expected_feature_count)
    ):
        raise ValueError(
            "Unexpected feature count. "
            f"Expected {expected_feature_count}, found {X.shape[1]}."
        )

    print(f"Selected features:     {X.shape[1]}")
    print(f"Age included:          {'age' in X.columns}")

    # 3. Reproduce the Week 6/7 stratified 80/20 split.
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=float(config["training"].get("test_size", 0.20)),
        random_state=int(config["training"].get("random_state", 42)),
        stratify=y,
    )

    print(f"Training set shape:    {X_train.shape}")
    print(f"Test set shape:        {X_test.shape}")

    # 4. Build the one pinned model from config.yaml.
    model = build_model(
        random_state=int(config["training"].get("random_state", 42))
    )

    print(f"Model:                 {config['model']['name']}")
    print("Training model...")

    train_start = time.perf_counter()
    model = train_model(model, X_train, y_train)
    training_seconds = time.perf_counter() - train_start

    # 5. Evaluate using the Week 7 headline metrics.
    metrics = evaluate_model(
        model,
        X_test,
        y_test,
    )
    metrics["training_time_seconds"] = training_seconds
    metrics["n_training_rows"] = int(len(X_train))
    metrics["n_test_rows"] = int(len(X_test))
    metrics["n_features"] = int(X.shape[1])

    print("\nEvaluation results")
    print("-" * 68)
    print(f"Accuracy:               {metrics['accuracy']:.3f}")
    print(f"Macro precision:        {metrics['macro_precision']:.3f}")
    print(f"Macro recall:           {metrics['macro_recall']:.3f}")
    print(f"Macro F1:               {metrics['macro_f1']:.3f}")
    print(f"ESI 1 recall:           {metrics['esi_1_recall']:.3f}")
    print(f"ESI 2 recall:           {metrics['esi_2_recall']:.3f}")
    print(f"ESI 3 recall:           {metrics['esi_3_recall']:.3f}")
    print(f"Training time:          {training_seconds:.2f} seconds")
    print(
        "Mean inference time:   "
        f"{metrics['mean_inference_time_ms']:.5f} ms/patient"
    )

    # 6. Save the fitted pipeline and its audit metrics.
    model_path.parent.mkdir(parents=True, exist_ok=True)
    save_model(model, model_path)
    save_metrics(metrics, metrics_path)

    print("\nSaved outputs")
    print("-" * 68)
    print(f"Model:   {model_path}")
    print(f"Metrics: {metrics_path}")
    print("\nTraining pipeline completed successfully.")


if __name__ == "__main__":
    main()

"""Train and evaluate the final CariSurg Logistic Regression model.

Run from the repository root:

    python scripts/train.py
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd
import yaml

# Allow imports from src/ when this file is run directly.
REPO_ROOT = Path(__file__).resolve().parents[1]

if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.data import clean_data, load_data, split_data
from src.features import select_final_features
from src.model import build_model, fit_and_evaluate, save_model


def parse_args() -> argparse.Namespace:
    """Read command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Train the final CariSurg Logistic Regression model."
    )

    parser.add_argument(
        "--config",
        type=Path,
        default=REPO_ROOT / "config.yaml",
        help="Path to the YAML configuration file.",
    )

    return parser.parse_args()


def load_config(config_path: Path) -> dict:
    """Load the project configuration."""
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with config_path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    if not isinstance(config, dict):
        raise ValueError("config.yaml must contain a YAML mapping.")

    return config


def resolve_path(path_value: str | Path) -> Path:
    """Resolve paths relative to the repository root."""
    path = Path(path_value)

    if path.is_absolute():
        return path

    return REPO_ROOT / path


def main() -> None:
    """Run the complete Logistic Regression training pipeline."""
    args = parse_args()
    config = load_config(args.config)

    seed = int(config.get("seed", 42))

    data_config = config["data"]
    model_config = config["model"]
    output_config = config["outputs"]

    data_path = resolve_path(data_config["raw_path"])
    output_directory = resolve_path(
        output_config.get("directory", "outputs")
    )

    model_path = output_directory / output_config.get(
        "model_file",
        "logistic_regression.joblib",
    )

    results_path = output_directory / output_config.get(
        "results_file",
        "model_results.csv",
    )

    print("=" * 68)
    print("CariSurg ED Triage — Logistic Regression")
    print("=" * 68)
    print(f"Dataset: {data_path}")
    print(f"Seed:    {seed}")

    # 1. Load the dataset.
    raw_df = load_data(data_path)

    print(f"Raw dataset shape:   {raw_df.shape}")

    # 2. Apply the final cleaning procedure.
    clean_df = clean_data(raw_df)

    print(f"Clean dataset shape: {clean_df.shape}")

    # 3. Select the final feature set:
    # original eligible features plus age.
    X, y, feature_names = select_final_features(clean_df)

    print(f"Selected features:   {len(feature_names)}")
    print(f"Age included:        {'age' in feature_names}")

    # 4. Create the reproducible stratified 80/20 split.
    X_train, X_test, y_train, y_test = split_data(
        X,
        y,
        test_size=float(data_config.get("test_size", 0.20)),
        random_state=seed,
    )

    print(f"Training set shape:  {X_train.shape}")
    print(f"Test set shape:      {X_test.shape}")

    # 5. Confirm that Logistic Regression is selected.
    model_name = model_config.get("name", "logistic_regression")

    if model_name != "logistic_regression":
        raise ValueError(
            "This training script is pinned to logistic_regression. "
            f"Found model.name={model_name!r}."
        )

    # 6. Build, train and evaluate the model.
    model = build_model(random_state=seed)

    print("\nTraining Logistic Regression...")

    fitted_model, metrics = fit_and_evaluate(
        model,
        X_train,
        y_train,
        X_test,
        y_test,
    )

    # 7. Save the model and evaluation results.
    output_directory.mkdir(parents=True, exist_ok=True)

    save_model(fitted_model, model_path)
    pd.DataFrame([metrics]).to_csv(results_path, index=False)

    print("\nEvaluation results")
    print("-" * 68)
    print(f"Accuracy:        {metrics['Accuracy']:.3f}")
    print(f"Macro precision: {metrics['Macro Precision']:.3f}")
    print(f"Macro recall:    {metrics['Macro Recall']:.3f}")
    print(f"Macro F1:        {metrics['Macro-F1']:.3f}")
    print(f"ESI 1 recall:    {metrics['ESI 1 Recall']:.3f}")
    print(f"ESI 2 recall:    {metrics['ESI 2 Recall']:.3f}")
    print(f"ESI 3 recall:    {metrics['ESI 3 Recall']:.3f}")
    print(
        "Training time:  "
        f"{metrics['Training Time (seconds)']:.2f} seconds"
    )

    print("\nSaved outputs")
    print("-" * 68)
    print(f"Model:   {model_path}")
    print(f"Results: {results_path}")
    print("\nTraining completed successfully.")


if __name__ == "__main__":
    main()

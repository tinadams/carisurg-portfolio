"""Shared helpers used across the project."""

from pathlib import Path

import pandas as pd


def save_results(results: dict, path: str | Path) -> None:
    """Save one model's metrics as a CSV file."""
    pd.DataFrame([results]).to_csv(path, index=False)


def print_results(results: dict) -> None:
    """Print the main evaluation results clearly."""
    print(f"Model: {results['Model']}")
    print(f"Accuracy: {results['Accuracy']:.3f}")
    print(f"Macro-F1: {results['Macro-F1']:.3f}")
    print(f"ESI 1 recall: {results['ESI 1 Recall']:.3f}")
    print(f"ESI 2 recall: {results['ESI 2 Recall']:.3f}")
    print(
        "Training time:",
        f"{results['Training Time (seconds)']:.2f} seconds",
    )


def ensure_directory(path: str | Path) -> Path:
    """Create an output directory when it does not already exist."""
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


"""Shared helper functions used across the project."""

from pathlib import Path

import pandas as pd


def save_results(results: dict, path: str | Path) -> None:
    """Save one model's evaluation metrics as a CSV file."""

    # Convert the results dictionary into a one-row DataFrame
    results_df = pd.DataFrame([results])

    # Save the table without adding a separate index column
    results_df.to_csv(path, index=False)


def print_results(results: dict) -> None:
    """Print the main evaluation results clearly."""

    # Display the model name
    print(f"Model: {results['Model']}")

    # Display the main overall performance measures
    print(f"Accuracy: {results['Accuracy']:.3f}")
    print(f"Macro-F1: {results['Macro-F1']:.3f}")

    # Display recall for the two most clinically urgent ESI levels
    print(f"ESI 1 recall: {results['ESI 1 Recall']:.3f}")
    print(f"ESI 2 recall: {results['ESI 2 Recall']:.3f}")

    # Display the total model training time
    print(
        "Training time:",
        f"{results['Training Time (seconds)']:.2f} seconds",
    )


def ensure_directory(path: str | Path) -> Path:
    """Create an output directory when it does not already exist."""

    # Convert the supplied path into a Path object
    directory = Path(path)

    # Create the directory and any missing parent folders
    # exist_ok=True prevents an error if the directory already exists
    directory.mkdir(parents=True, exist_ok=True)

    # Return the directory path for later use
    return directory

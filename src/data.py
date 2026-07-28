"""Load, clean, and split the emergency-triage dataset."""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


# Vital-sign columns required for cleaning and modelling
VITALS = [
    "triage_vital_hr",      # Heart rate
    "triage_vital_sbp",     # Systolic blood pressure
    "triage_vital_dbp",     # Diastolic blood pressure
    "triage_vital_rr",      # Respiratory rate
    "triage_vital_o2",      # Oxygen saturation
    "triage_vital_temp",    # Temperature
    "triage_glucose",       # Blood glucose
]

# Name of the prediction target
TARGET = "esi"


def load_data(path: str | Path) -> pd.DataFrame:
    """Load the raw CSV file."""

    # Convert the supplied path into a Path object
    path = Path(path)

    # Stop with a clear error if the dataset cannot be found
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    # Read and return the CSV as a pandas DataFrame
    return pd.read_csv(path)


def clean_data(df_raw: pd.DataFrame) -> pd.DataFrame:
    """Apply the cleaning steps used in the final notebook."""

    # Check that all columns required for cleaning are present
    required = VITALS + [TARGET, "age", "gender"]
    missing = [column for column in required if column not in df_raw.columns]

    # Stop if one or more required columns are missing
    if missing:
        raise ValueError(f"Required columns are missing: {missing}")

    # Work on a copy so the original DataFrame is not changed
    df = df_raw.copy()

    # Remove accidental index columns created when saving CSV files
    df = df.drop(
        columns=[c for c in df.columns if c.startswith("Unnamed")],
        errors="ignore",
    )

    # Convert vital signs and age to numeric values
    # Invalid text values are replaced with missing values
    for column in VITALS + ["age"]:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # Convert the ESI target to numeric
    df[TARGET] = pd.to_numeric(df[TARGET], errors="coerce")

    # Keep only valid ESI levels from 1 to 5
    df = df[df[TARGET].isin([1, 2, 3, 4, 5])].copy()

    # Replace unrealistic temperature values with missing values
    df.loc[
        (df["triage_vital_temp"] < 90)
        | (df["triage_vital_temp"] > 110),
        "triage_vital_temp",
    ] = np.nan

    # Replace impossible oxygen-saturation values with missing values
    df.loc[
        (df["triage_vital_o2"] < 0)
        | (df["triage_vital_o2"] > 100),
        "triage_vital_o2",
    ] = np.nan

    # Standardize gender text and convert it to numeric values
    df["gender"] = (
        df["gender"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map({
            "male": 0,
            "m": 0,
            "female": 1,
            "f": 1,
        })
    )

    # Fill missing numeric values with the median for each column
    for column in VITALS + ["age", "gender"]:
        df[column] = df[column].fillna(df[column].median())

    # Store ESI levels as integers
    df[TARGET] = df[TARGET].astype(int)

    # Return the cleaned dataset
    return df


def split_data(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.20,
    random_state: int = 42,
):
    """Create the reproducible stratified train-test split."""

    # Split the features and target into training and test sets
    return train_test_split(
        X,
        y,
        test_size=test_size,        # Use 20% of the data for testing
        stratify=y,                 # Preserve the ESI class proportions
        random_state=random_state,  # Produce the same split each time
    )

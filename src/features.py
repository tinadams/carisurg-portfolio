"""Select final model inputs and create optional clinical features."""

import numpy as np
import pandas as pd


# Name of the target column the model will predict
TARGET = "esi"


# Demographic columns excluded from the original eligible feature set
# Age is added back later because it improved the final Logistic Regression result
DEMOGRAPHICS = [
    "age",
    "gender",
    "ethnicity",
    "race",
    "lang",
    "religion",
    "maritalstatus",
    "employstatus",
    "insurance_status",
]


# Administrative columns excluded because they are not direct clinical measurements
ADMIN = [
    "dep_name",
    "arrivalmode",
    "arrivalmonth",
    "arrivalday",
    "arrivalhour_bin",
]


# Columns excluded because they contain information recorded after triage
# Including them could cause data leakage
LEAKAGE = [
    "disposition",
    "previousdispo",
]


def select_final_features(df: pd.DataFrame):
    """Return the final controlled feature set: eligible features plus age."""

    # Select all columns except the target, leakage variables,
    # administrative fields, and demographic variables
    original = [
        column
        for column in df.columns
        if column != TARGET
        and column not in LEAKAGE + ADMIN + DEMOGRAPHICS
    ]

    # Add age back because the controlled feature experiment showed
    # that original eligible features plus age performed best
    # dict.fromkeys removes any duplicate column names while keeping order
    final_features = list(dict.fromkeys(original + ["age"]))

    # Create the model input table using the selected feature columns
    X = df[final_features].copy()

    # Create the target series containing the true ESI levels
    y = df[TARGET].copy()

    # Identify any non-numeric columns that cannot be passed directly
    # into the final Logistic Regression pipeline
    non_numeric = X.select_dtypes(exclude=np.number).columns.tolist()

    # Stop with a clear message if non-numeric inputs remain
    if non_numeric:
        raise TypeError(f"Non-numeric model inputs found: {non_numeric}")

    # Return the model inputs, target, and selected feature names
    return X, y, final_features


def add_clinical_features(data: pd.DataFrame) -> pd.DataFrame:
    """Create the optional engineered features tested in Week 7."""

    # Work on a copy so the original input data is not changed
    out = data.copy()

    # Replace zero systolic blood pressure values with missing values
    # to prevent division by zero when calculating shock index
    systolic_bp = out["triage_vital_sbp"].replace(0, np.nan)

    # Calculate shock index as heart rate divided by systolic blood pressure
    out["shock_index"] = (
        out["triage_vital_hr"] / systolic_bp
    )

    # Calculate the difference between systolic and diastolic blood pressure
    out["pulse_pressure"] = (
        out["triage_vital_sbp"]
        - out["triage_vital_dbp"]
    )

    # Estimate mean arterial pressure using diastolic pressure
    # plus one-third of the pulse pressure
    out["map_estimate"] = (
        out["triage_vital_dbp"]
        + out["pulse_pressure"] / 3
    )

    # Flag patients with a respiratory rate above 20 breaths per minute
    out["is_tachypneic"] = (
        out["triage_vital_rr"] > 20
    ).astype(int)

    # Flag patients with oxygen saturation below 92%
    out["is_hypoxic"] = (
        out["triage_vital_o2"] < 92
    ).astype(int)

    # Flag patients with a temperature of at least 100.4°F
    out["is_febrile"] = (
        out["triage_vital_temp"] >= 100.4
    ).astype(int)

    # Count how many of the three clinical warning flags are present
    out["red_flag_count"] = out[
        [
            "is_tachypneic",
            "is_hypoxic",
            "is_febrile",
        ]
    ].sum(axis=1)

    # Replace positive or negative infinity with missing values
    out = out.replace(
        [np.inf, -np.inf],
        np.nan,
    )

    # Fill missing numeric values with the median of each column
    return out.fillna(
        out.median(numeric_only=True)
    )

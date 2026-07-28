"""Select final inputs and create optional clinical features."""

import numpy as np
import pandas as pd

TARGET = "esi"

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

ADMIN = [
    "dep_name",
    "arrivalmode",
    "arrivalmonth",
    "arrivalday",
    "arrivalhour_bin",
]

LEAKAGE = ["disposition", "previousdispo"]


def select_final_features(df: pd.DataFrame):
    """Return the final controlled feature set: eligible features plus age."""
    original = [
        column
        for column in df.columns
        if column != TARGET
        and column not in LEAKAGE + ADMIN + DEMOGRAPHICS
    ]
    final_features = list(dict.fromkeys(original + ["age"]))

    X = df[final_features].copy()
    y = df[TARGET].copy()

    non_numeric = X.select_dtypes(exclude=np.number).columns.tolist()
    if non_numeric:
        raise TypeError(f"Non-numeric model inputs found: {non_numeric}")

    return X, y, final_features


def add_clinical_features(data: pd.DataFrame) -> pd.DataFrame:
    """Create the optional engineered features tested in Week 7."""
    out = data.copy()

    systolic_bp = out["triage_vital_sbp"].replace(0, np.nan)

    out["shock_index"] = out["triage_vital_hr"] / systolic_bp
    out["pulse_pressure"] = (
        out["triage_vital_sbp"] - out["triage_vital_dbp"]
    )
    out["map_estimate"] = (
        out["triage_vital_dbp"] + out["pulse_pressure"] / 3
    )
    out["is_tachypneic"] = (out["triage_vital_rr"] > 20).astype(int)
    out["is_hypoxic"] = (out["triage_vital_o2"] < 92).astype(int)
    out["is_febrile"] = (out["triage_vital_temp"] >= 100.4).astype(int)
    out["red_flag_count"] = out[
        ["is_tachypneic", "is_hypoxic", "is_febrile"]
    ].sum(axis=1)

    out = out.replace([np.inf, -np.inf], np.nan)
    return out.fillna(out.median(numeric_only=True))


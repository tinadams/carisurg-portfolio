"""Build, train, evaluate, and save the final Logistic Regression model."""

from pathlib import Path
import time

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def build_model(random_state: int = 42):
    """Return the selected Phase 3 Logistic Regression pipeline."""
    return make_pipeline(
        StandardScaler(),
        LogisticRegression(
            max_iter=1000,
            random_state=random_state,
        ),
    )


def train_model(model, X_train: pd.DataFrame, y_train: pd.Series):
    """Fit and return the model."""
    return model.fit(X_train, y_train)


def evaluate_model(
    model,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    name: str = "Logistic Regression",
    clarity: str = "High",
) -> dict:
    """Measure the final benchmark metrics."""
    start = time.perf_counter()
    predictions = model.predict(X_test)
    inference_seconds = time.perf_counter() - start

    esi_recall = recall_score(
        y_test,
        predictions,
        labels=[1, 2, 3],
        average=None,
        zero_division=0,
    )

    return {
        "Model": name,
        "Accuracy": accuracy_score(y_test, predictions),
        "Macro Precision": precision_score(
            y_test, predictions, average="macro", zero_division=0
        ),
        "Macro Recall": recall_score(
            y_test, predictions, average="macro", zero_division=0
        ),
        "Macro-F1": f1_score(
            y_test, predictions, average="macro", zero_division=0
        ),
        "ESI 1 Recall": esi_recall[0],
        "ESI 2 Recall": esi_recall[1],
        "ESI 3 Recall": esi_recall[2],
        "Inference Time per Prediction (ms)": (
            inference_seconds / len(X_test)
        ) * 1000,
        "Clarity": clarity,
    }


def fit_and_evaluate(
    model,
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
) -> tuple[object, dict]:
    """Train once, record training time, and evaluate."""
    start = time.perf_counter()
    fitted_model = train_model(model, X_train, y_train)
    training_seconds = time.perf_counter() - start

    results = evaluate_model(fitted_model, X_test, y_test)
    results["Training Time (seconds)"] = training_seconds
    return fitted_model, results


def save_model(model, path: str | Path) -> None:
    """Save the fitted model for later use."""
    joblib.dump(model, Path(path))


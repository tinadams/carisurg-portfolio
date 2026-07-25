from time import perf_counter
from typing import Any

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)


def create_model(
    model_name: str,
    hyperparameters: dict[str, Any],
):
    """Create the selected model using the configured hyperparameters."""
    if model_name == "logistic_regression":
        return LogisticRegression(**hyperparameters)

    raise ValueError(f"Unsupported model: {model_name}")


def train_model(model, X_train: pd.DataFrame, y_train: pd.Series):
    """Train the model and return its training time."""
    start_time = perf_counter()
    model.fit(X_train, y_train)
    training_time = perf_counter() - start_time

    return model, training_time


def evaluate_model(model, X_test: pd.DataFrame, y_test: pd.Series) -> dict:
    """Evaluate the model and return headline metrics."""
    start_time = perf_counter()
    predictions = model.predict(X_test)
    inference_time = perf_counter() - start_time

    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "macro_precision": precision_score(
            y_test,
            predictions,
            average="macro",
            zero_division=0,
        ),
        "macro_recall": recall_score(
            y_test,
            predictions,
            average="macro",
            zero_division=0,
        ),
        "macro_f1": f1_score(
            y_test,
            predictions,
            average="macro",
            zero_division=0,
        ),
        "weighted_f1": f1_score(
            y_test,
            predictions,
            average="weighted",
            zero_division=0,
        ),
        "inference_time_seconds": inference_time,
    }

    return metrics

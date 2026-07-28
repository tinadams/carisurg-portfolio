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

    # Create a pipeline that first scales the input features
    # and then trains the Logistic Regression model
    return make_pipeline(
        StandardScaler(),
        LogisticRegression(
            max_iter=1000,          # Allow enough iterations for convergence
            random_state=random_state,  # Keep results reproducible
        ),
    )


def train_model(model, X_train: pd.DataFrame, y_train: pd.Series):
    """Fit and return the model."""

    # Train the model using the training features and target labels
    return model.fit(X_train, y_train)


def evaluate_model(
    model,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    name: str = "Logistic Regression",
    clarity: str = "High",
) -> dict:
    """Measure the final benchmark metrics."""

    # Record the start time before generating predictions
    start = time.perf_counter()

    # Predict ESI levels for the test set
    predictions = model.predict(X_test)

    # Calculate the total prediction time
    inference_seconds = time.perf_counter() - start

    # Calculate recall separately for ESI levels 1, 2, and 3
    esi_recall = recall_score(
        y_test,
        predictions,
        labels=[1, 2, 3],
        average=None,
        zero_division=0,
    )

    # Return all evaluation results in one dictionary
    return {
        "Model": name,

        # Overall proportion of correct predictions
        "Accuracy": accuracy_score(y_test, predictions),

        # Average precision across all five ESI levels
        "Macro Precision": precision_score(
            y_test,
            predictions,
            average="macro",
            zero_division=0,
        ),

        # Average recall across all five ESI levels
        "Macro Recall": recall_score(
            y_test,
            predictions,
            average="macro",
            zero_division=0,
        ),

        # Balanced performance score across all five ESI levels
        "Macro-F1": f1_score(
            y_test,
            predictions,
            average="macro",
            zero_division=0,
        ),

        # Recall for the three most urgent ESI levels
        "ESI 1 Recall": esi_recall[0],
        "ESI 2 Recall": esi_recall[1],
        "ESI 3 Recall": esi_recall[2],

        # Average prediction time for one patient, in milliseconds
        "Inference Time per Prediction (ms)": (
            inference_seconds / len(X_test)
        ) * 1000,

        # Plain-language rating of how easy the model is to explain
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

    # Record the start time before training begins
    start = time.perf_counter()

    # Fit the model on the training data
    fitted_model = train_model(model, X_train, y_train)

    # Calculate the total training time
    training_seconds = time.perf_counter() - start

    # Evaluate the fitted model on the test data
    results = evaluate_model(
        fitted_model,
        X_test,
        y_test,
    )

    # Add training time to the results dictionary
    results["Training Time (seconds)"] = training_seconds

    # Return both the fitted model and its evaluation results
    return fitted_model, results


def save_model(model, path: str | Path) -> None:
    """Save the fitted model for later use."""

    # Convert the supplied file path into a Path object
    path = Path(path)

    # Save the complete fitted pipeline to disk
    joblib.dump(model, path)

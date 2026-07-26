from pathlib import Path

import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load the emergency department triage dataset from a CSV file.

    Parameters
    ----------
    file_path : str
        Path to the CSV dataset.

    Returns
    -------
    pd.DataFrame
        The loaded dataset.
    """

    # Convert the file path into a Path object so we can check it safely.
    path = Path(file_path)

    # Stop immediately and show a clear error if the file cannot be found.
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")

    # Read the CSV file into a pandas DataFrame.
    dataframe = pd.read_csv(path)

    # Stop the pipeline if the file exists but contains no rows.
    if dataframe.empty:
        raise ValueError("The dataset was loaded, but it contains no rows.")

    # Return the loaded dataset so other parts of the project can use it.
    return dataframe


def validate_schema(
    dataframe: pd.DataFrame,
    feature_columns: list[str],
    target_column: str,
) -> None:
    """
    Check that the dataset contains all required feature and target columns.
    """

    # Combine the feature columns and target column into one expected list.
    required_columns = feature_columns + [target_column]

    # Identify any expected columns that are missing from the dataset.
    missing_columns = [
        column
        for column in required_columns
        if column not in dataframe.columns
    ]

    # Raise a clear error if one or more required columns are missing.
    if missing_columns:
        raise ValueError(
            f"The dataset is missing required columns: {missing_columns}"
        )


def prepare_data(
    dataframe: pd.DataFrame,
    feature_columns: list[str],
    target_column: str,
) -> tuple[pd.DataFrame, pd.Series]:
    """
    Select the model features and target variable.

    Rows with a missing target value are removed.
    """

    # Check that the dataset has every column needed by the model.
    validate_schema(
        dataframe=dataframe,
        feature_columns=feature_columns,
        target_column=target_column,
    )

    # Keep only the feature columns and target column needed for modelling.
    selected_columns = feature_columns + [target_column]
    model_data = dataframe[selected_columns].copy()

    # Remove rows where the true ESI label is missing.
    # The model cannot learn from a row without a known target value.
    model_data = model_data.dropna(subset=[target_column])

    # X contains the input variables used to make predictions.
    X = model_data[feature_columns]

    # y contains the correct ESI level the model is trying to predict.
    y = model_data[target_column]

    # Return the features and target separately for model training.
    return X, y

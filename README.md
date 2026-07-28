````markdown
# CariSurg Portfolio

**AI-assisted emergency department triage project using synthetic clinical data.**

## About

This 12-week CariSurg MedTech Pathways pilot explores the development of an AI-assisted emergency department triage tool in a Caribbean context.

The project began with de-identified Mercer General emergency department data for early cleaning and triage-rule practice. Later work used `yaleemmlc_admissionprediction_triage.csv`, which contains 55,121 emergency department encounters and 225 columns.

The project compared Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, a small MLP neural network and a stacked ensemble. Logistic Regression was selected as the primary Phase 3 model because it achieved the highest macro-F1, trained quickly and was easier to explain than the more complex models.

The final model uses the original eligible triage-time features plus age. Administrative fields and post-triage outcomes are excluded to prevent data leakage.

## Purpose

This repository organises notebooks, reusable Python modules, configuration files, written reports and model-evaluation outputs in a clear, reproducible and reviewable format.

The final model pipeline is stored in `src/` and can be run without manually executing notebook cells.

## Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/tinadams/carisurg-portfolio.git
cd carisurg-portfolio
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
````

Requires Python 3.10 or later.

Jupyter Notebook, JupyterLab or Google Colab is also required to run the exploratory notebooks.

## Usage

The datasets are not included in this repository.

Earlier notebooks use:

```python
FILE_PATH = "EmergencyTriageDataset_Reduced_Dirty.csv"
```

Later notebooks and the final model use:

```python
FILE_PATH = "yaleemmlc_admissionprediction_triage.csv"
```

To run the final model, place the larger dataset at:

```text
data/yaleemmlc_admissionprediction_triage.csv
```

The path can also be changed in `config.yaml`.

From the main repository folder, run:

```bash
python scripts/train.py
```

The script will:

1. read the settings from `config.yaml`;
2. load and clean the dataset;
3. select the final features;
4. create a stratified 80/20 train-test split;
5. train Logistic Regression;
6. evaluate and save the model.

The output files are saved in:

```text
outputs/
├── logistic_regression.joblib
└── model_results.csv
```

`logistic_regression.joblib` contains the trained model pipeline.

`model_results.csv` contains the final evaluation results.

## Configuration

The final model settings are stored in `config.yaml`.

```yaml
seed: 42

data:
  raw_path: "data/yaleemmlc_admissionprediction_triage.csv"
  target: "esi"
  test_size: 0.20

features:
  use_engineered_features: false
  include_age: true

model:
  name: "logistic_regression"
  max_iter: 1000

outputs:
  directory: "outputs"
  model_file: "logistic_regression.joblib"
  results_file: "model_results.csv"
```

The seed and train-test split are fixed to support reproducibility.

Engineered clinical features are turned off because the original eligible features plus age produced stronger macro-F1 and ESI 1 recall.

## Repository Structure

```text
carisurg-portfolio/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── config.yaml
├── scripts/
│   └── train.py
├── src/
│   ├── __init__.py
│   ├── data.py
│   ├── features.py
│   ├── model.py
│   └── utils.py
├── notebooks/
│   └── project notebooks
├── docs/
│   └── reports, memos and model-selection records
├── data/
│   └── README.md
└── outputs/
    └── generated model and results files
```

## Folder Guide

* `notebooks/` contains the exploratory analysis, baseline models, feature experiments, tuning and error analysis.
* `docs/` contains reports, proposals, ethics and risk work, the cost-benefit memo and model-selection records.
* `data/` contains dataset instructions and is the expected location for the CSV file.
* `src/data.py` loads, checks, cleans and splits the dataset.
* `src/features.py` selects the final inputs and contains optional engineered features.
* `src/model.py` builds, trains, evaluates and saves Logistic Regression.
* `src/utils.py` contains shared helper functions.
* `scripts/train.py` reads `config.yaml` and runs the full pipeline.
* `requirements.txt` lists the required Python packages.

## Model Evaluation

The baseline evaluation compared a stratified Dummy Classifier, Logistic Regression and a Decision Tree. Logistic Regression performed best overall but identified only 4 of the 16 ESI Level 1 patients in the test set.

The final controlled comparison evaluated:

* Logistic Regression
* Untuned Random Forest
* Tuned Random Forest
* Gradient Boosting
* Small MLP neural network
* Stacked Ensemble

All models used the same feature set and train-test split.

Logistic Regression achieved:

* Accuracy: `0.683`
* Macro-F1: `0.508`
* ESI 1 recall: `0.250`
* ESI 2 recall: `0.626`
* ESI 3 recall: `0.770`
* Training time: approximately `6.2 seconds`

It achieved the highest macro-F1 and required less training time than the more complex models. The tuned Random Forest remains as a comparison model.

These results are experimental and do not support clinical deployment. Further validation, fairness assessment and review of undertriage and overtriage are required.

## Version Control Workflow

Major edits are made through a feature branch and merged into `main` using a pull request. This keeps the project history clear and makes changes easier to review.

## Contributing

This repository is part of the CariSurg Healthcare AI Program coursework. Contributions are not currently expected, but suggestions are welcome.

## Licence

This project is licensed under the MIT Licence. See `LICENSE` for details.

```
```

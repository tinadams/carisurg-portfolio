# CariSurg Portfolio

**AI-assisted emergency department triage project using synthetic clinical data.**

## About

This 12-week CariSurg MedTech Pathways pilot focuses on developing an AI-assisted emergency department triage tool in a Caribbean context, where triage decisions often rely on manual clinical judgement.

The project began with de-identified Mercer General emergency department data for early clinical data-cleaning and triage-rule practice. Later notebooks use a larger emergency department triage dataset, `yaleemmlc_admissionprediction_triage.csv`, which contains 55,121 emergency department arrival records and 225 columns. This larger dataset supports exploratory analysis, feasibility assessment and baseline machine-learning development.

The initial baseline evaluation compared logistic regression and a decision tree against a stratified dummy classifier. Logistic regression performed best overall, although its performance was considerably weaker for the rare ESI Levels 1 and 5. Further analysis examined the ESI Level 1 patients that the model correctly identified and missed.

This repository organises notebooks, written deliverables, workflow documents, proposals, feasibility memos and model-evaluation figures in one place for future project work.

## Purpose

The purpose of this repository is to organise the project materials in a clear, reproducible and reviewable format.

## Installation

To run the notebooks locally, clone the repository and install the required packages:

```bash
git clone https://github.com/tinadams/carisurg-portfolio.git
cd carisurg-portfolio
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Requires Python 3.x and Jupyter Notebook, JupyterLab or Google Colab.

## Usage

The datasets are not included in this repository, so the relevant dataset must be added before running the notebooks.

Earlier notebooks use the Mercer General ED dataset:

```python
FILE_PATH = "EmergencyTriageDataset_Reduced_Dirty.csv"
```

Later notebooks use the larger triage and admission-prediction dataset:

```python
FILE_PATH = "yaleemmlc_admissionprediction_triage.csv"
```

The relevant CSV file should be placed in the same location where the notebook is being run unless the file path is updated.

When using Google Colab, upload the CSV file into the Colab session before running the notebook.

When running the notebooks locally, place the CSV file in the same folder as the notebook or update the file path to its saved location.

The baseline model notebooks use a stratified 80/20 train-test split with `random_state=42` to support reproducibility.

## Repository Structure

```text
carisurg-portfolio/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── notebooks/
│   ├── week_0_day_1_clean_gender_column.ipynb
│   ├── week_0_day_2_clean_fio2_column.ipynb
│   ├── week_0_day_3_data_visualisation.ipynb
│   ├── week_5_Tutorial1_Clinical_Data_Literacy_STUDENT.ipynb
│   ├── week_5_Tutorial2_Data_Profiling_STUDENT.ipynb
│   ├── week_5_Tutorial3_Exploratory_Visualisation_STUDENT.ipynb
│   ├── week_6_Tutorial2_Implement_LR_and_DT_STUDENT.ipynb
│   └── week_6_Tutorial3_Model_Evaluation_STUDENT.ipynb
├── docs/
│   ├── risk_register.md
│   ├── week_0_day_4_Vital_Sign_Description_(BP).pdf
│   ├── week_0_day_5_Vital_Sign_Description_(SpO2).pdf
│   ├── week_0_day_6_Triage_Pseudocode.pdf
│   ├── week_1_Proposal.pdf
│   ├── week_2_Proposal.pdf
│   ├── week_3_Workflow_Diagram.md
│   ├── week_3_proposal.pdf
│   ├── week_4_ethics_risk_interim.pdf
│   ├── week_5_Exploration_and_Feasibility_Memo_FINAL.pdf
│   ├── week_5_Exploration_and_Feasibility_Memo_OUTLINE.pdf
│   ├── Baseline_Model_Report_Final.pdf
│   ├── w6_confusion_logreg.png
│   ├── w6_confusion_tree.png
│   └── logreg_recall_all_esi_levels.png
├── data/
│   └── README.md
└── src/
    └── README.md
```

## Folder Guide

* `notebooks/` contains Jupyter notebooks for clinical data cleaning, data literacy, data profiling, exploratory visualisation, baseline model implementation and model evaluation.
* `docs/` contains written deliverables, research proposals, workflow documentation, ethics and risk work, the exploration and feasibility memo, the final baseline model report and model-evaluation figures.
* `data/` is reserved for dataset instructions and future dataset storage. The datasets are not currently included in this repository.
* `src/` is reserved for reusable Python modules and scripts that may be developed later in the program.
* `requirements.txt` lists the Python libraries needed to run the notebooks.

## Baseline Model Evaluation

The baseline evaluation includes:

* A stratified dummy classifier used as a random-guess comparison.
* A logistic regression model with scaled numeric features.
* A decision tree limited to `max_depth=5`.
* Accuracy, per-class precision, recall and F1 scores.
* Macro and weighted F1 comparisons.
* Confusion matrices for logistic regression and the decision tree.
* Recall comparisons across all five ESI levels.
* A closer review of the ESI Level 1 cases that logistic regression correctly identified and missed.

Recall for ESI Level 1 was selected as the primary metric because it measures how many of the most critical patients the model correctly identifies. Overall accuracy can appear strong on an imbalanced dataset even when a model misses patients requiring immediate treatment.

Logistic regression performed best overall but correctly identified only 4 of the 16 ESI Level 1 patients in the test set. The decision tree and dummy classifier did not correctly identify any ESI Level 1 patients. These results show that further work is needed before either trained model could be considered for clinical use.

## Version Control Workflow

Major edits are made through a feature branch and merged into `main` using a pull request. This keeps the project history clear and supports a more reviewable workflow.

## Contributing

This repository is part of the CariSurg Healthcare AI Program coursework. Contributions are not currently expected, but suggestions for improvement are welcome.

## Licence

This project is licensed under the MIT Licence. See `LICENSE` for details.

# CariSurg Portfolio

**AI-assisted emergency department triage project using synthetic clinical data.**

## About

This 12-week CariSurg MedTech Pathways pilot focuses on developing an AI-assisted emergency department triage tool in a Caribbean context, where triage decisions often rely on manual clinical judgement.

The project currently uses de-identified Mercer General emergency department data and emergency department triage data for exploratory analysis, feasibility assessment, and early machine learning preparation. This repository organises weekly notebooks, written deliverables, workflow documents, proposals, and feasibility memos in one place for future project work.

## Purpose

The purpose of this repository is to organise the project materials in a clear, reproducible, and reviewable format.

## Installation

To run the notebooks locally, clone the repository and install the required packages:

```bash
git clone https://github.com/tinadams/carisurg-portfolio.git
cd carisurg-portfolio
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Requires Python 3.x and Jupyter Notebook, JupyterLab, or Google Colab.

## Usage

The dataset is not included in this repository, you must add it before running the notebooks.

Some earlier notebooks use the Mercer General ED dataset:

```python
FILE_PATH = "EmergencyTriageDataset_Reduced_Dirty.csv"
```

Some later notebooks may use the larger triage/admission prediction dataset:

```python
FILE_PATH = "yaleemmlc_admissionprediction_triage.csv"
```

This means the relevant CSV file needs to be in the same place where the notebook is being run, unless the file path is updated.

If you are using Google Colab, upload the CSV file into the Colab session before running the notebook.

If you are running the notebooks locally, put the CSV file in the same folder as the notebook, or update the file path if you store it somewhere else.

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
│   └── week_5_Tutorial3_Exploratory_Visualisation_STUDENT.ipynb
├── docs/
│   ├── risk-register.md
│   ├── week_0_day_4_Vital_Sign_Description_(BP).pdf
│   ├── week_0_day_5_Vital_Sign_Description_(SpO2).pdf
│   ├── week_0_day_6_Triage_Pseudocode.pdf
│   ├── week_1_Proposal.pdf
│   ├── week_2_Proposal.pdf
│   ├── week_3_Workflow_Diagram.md
│   ├── week_3_proposal.pdf
│   ├── week_4_ethics_risk_interim.pdf
│   ├── week_5_Exploration_and_Feasibility_Memo_FINAL.pdf
│   └── week_5_Exploration_and_Feasibility_Memo_OUTLINE.pdf
├── data/
│   └── README.md
└── src/
    └── README.md
```

## Folder Guide

* `notebooks/` contains Jupyter notebooks for clinical data cleaning, data literacy, data profiling, and exploratory visualisation.
* `docs/` contains Week 0 deliverables, research proposals, workflow documentation, ethics/risk work, and the Week 5 exploration and feasibility memo.
* `data/` is reserved for dataset instructions and future dataset storage. The datasets are not currently included in this repository.
* `src/` is reserved for reusable Python modules and scripts that may be developed later in the program.
* `requirements.txt` lists the Python libraries needed to run the notebooks.

## Version Control Workflow

Major edits are made through a feature branch and merged into `main` using a pull request. This keeps the project history clear and supports a more reviewable workflow.

## Contributing

This repository is part of the CariSurg Healthcare AI Program coursework. Contributions are not currently expected but suggestions for improvement are welcome.

## Licence

This project is licensed under the MIT Licence. See `LICENSE` for details.

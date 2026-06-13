# CariSurg Portfolio

**Artificial Intelligence-assisted emergency department triage project using synthetic clinical data.**

## About

This 12-week CariSurg MedTech Pathways pilot focuses on developing an AI-assisted emergency department triage system in a Caribbean context, where triage decisions often rely on manual clinical assessment and staff judgement.

The project currently uses synthetic Mercer General ED data, with plans to expand to a larger dataset as the pilot develops. The repository includes Week 0 clinical data notebooks, Week 1 research documents, and the project proposal as an organised foundation for future project development.

## Purpose

The purpose of this repository is to organise the project material in a clear and reproducible format.
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

Place the Mercer General Emergency Department CSV file in the `data/` folder:

```text
data/EmergencyTriageDataset_Reduced_Dirty.csv
```

Run a notebook from the repository root:

```bash
jupyter lab notebooks/week_0_day_1_clean_gender_column.ipynb
```

Recommended file path when running notebooks locally:

```python
FILE_PATH = "../data/EmergencyTriageDataset_Reduced_Dirty.csv"
```

File path in Google Colab, if the CSV is uploaded alongside the notebook:

```python
FILE_PATH = "EmergencyTriageDataset_Reduced_Dirty.csv"
```

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
│   └── week_0_day_3_data_visualisation.ipynb
├── docs/
│   ├── week_1_memo.pdf
│   └── week_1_proposal.pdf
├── data/
│   └── README.md
└── src/
    └── README.md
```

## Folder Guide

* `notebooks/` contains Week 0 Jupyter notebooks for clinical data cleaning and visualisation.
* `docs/` contains Week 1 research and proposal documents.
* `data/` is reserved for the Mercer General Emergency Department dataset. The dataset is not included in this repository.
* `src/` is reserved for reusable Python modules and scripts that may be developed later in the programme.
* `requirements.txt` lists the Python libraries needed to run the notebooks.

## Notes on Data

The dataset used in this project is synthetic and is not committed to the repository. When running the notebooks locally, the dataset should be placed in the `data/` folder.

## Version Control Workflow

Major edits are made through a feature branch and merged into `main` using a pull request. This keeps the project history clear and supports a more reviewable workflow.

## Licence

This project is licensed under the MIT Licence. See `LICENSE` for details.

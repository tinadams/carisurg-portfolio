# CariSurg Portfolio

**AI-assisted emergency department triage project using synthetic clinical data.**

## About

This 12-week CariSurg MedTech Pathways pilot focuses on developing an AI-assisted emergency department triage system in a Caribbean context, where triage decisions often rely on manual clinical assessment and staff judgement.

The project currently uses synthetic Mercer General ED data, with plans to expand to a larger dataset as the pilot develops. This repository keeps the Week 0 notebooks, Week 1 research documents, and project proposal organised in one place for future project work.

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

The dataset is not included in this repository and must be added locally before running the notebooks.

Place the Mercer General Emergency Department CSV file in the `data/` folder:

```text
data/EmergencyTriageDataset_Reduced_Dirty.csv
```

The notebooks are stored in the `notebooks/` folder and use the following relative file path to access the dataset:

```python
FILE_PATH = "../data/EmergencyTriageDataset_Reduced_Dirty.csv"
```

Open a notebook from the repository root using JupyterLab:

```bash
jupyter lab notebooks/week_0_day_1_clean_gender_column.ipynb
```

If running the notebooks in Google Colab, upload the CSV file into the Colab session or update the file path as needed.

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

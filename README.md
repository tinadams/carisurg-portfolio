# CariSurg Portfolio

This repo contains my CariSurg Healthcare AI Programme work: Week 0 clinical data notebooks and Week 1 research documents.

Week 0 covers Mercer General ED data cleaning and visualisation. Week 1 covers AI-assisted emergency triage and patient flow.

## Purpose

This repo lets CariSurg tutors, clinical reviewers, and technical reviewers inspect my work quickly.

## Installation

```bash
git clone https://github.com/tinadams/carisurg-portfolio.git
cd carisurg-portfolio
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Requires Python 3.x and Jupyter or Google Colab.

## Usage

Place the Mercer General ED CSV in `data/`:

```text
data/EmergencyTriageDataset_Reduced_Dirty.csv
```

Run a notebook from the repo root:

```bash
jupyter lab notebooks/week_0_day_1_clean_gender_column.ipynb
```

File path inside notebooks:

```python
FILE_PATH = "../data/EmergencyTriageDataset_Reduced_Dirty.csv"
```

File path in Google Colab (CSV alongside notebook):

```python
FILE_PATH = "EmergencyTriageDataset_Reduced_Dirty.csv"
```

## Repository Structure

```text
carisurg-portfolio/
├── README.md
├── LICENSE
├── requirements.txt
├── notebooks/
│   ├── week_0_day_1_clean_gender_column.ipynb
│   ├── week_0_day_2_clean_fio2_column.ipynb
│   └── week_0_day_3_data_visualisation.ipynb
├── docs/
│   ├── week_1_memo.docx
│   └── week_1_proposal.docx
└── data/
    └── README.md
```

## Contributing

Individual portfolio work. Major edits go through a feature branch and pull request.

## Licence

MIT. See `LICENSE`.

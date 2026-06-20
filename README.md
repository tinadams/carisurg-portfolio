# CariSurg Portfolio

**AI-assisted emergency department triage project using synthetic clinical data.**

## About

This 12-week CariSurg MedTech Pathways pilot focuses on developing an AI-assisted emergency department triage tool in a Caribbean context, where triage decisions often rely on manual clinical judgement.

The project currently uses de-identified Mercer General emergency department data, with plans to expand to a larger dataset as the pilot develops. This repository organises Week 0 notebooks, Week 0 deliverables, and Weeks 1 and 2 research proposal documents in one place for future project work.

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

All notebooks currently look for the dataset using this file path:

```python
FILE_PATH = "EmergencyTriageDataset_Reduced_Dirty.csv"
```

This means the CSV file needs to be in the same place where the notebook is being run.

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
│   └── week_0_day_3_data_visualisation.ipynb
├── docs/
│   ├── week_0_day_4_Vital_Sign_Description_(BP).pdf
│   ├── week_0_day_5_Vital_Sign_Description_(SpO2).pdf
│   ├── week_0_day_6_Triage_Pseudocode.pdf
│   ├── week_1_proposal.pdf
│   └── week_2_proposal.pdf
├── data/
│   └── README.md
└── src/
    └── README.md
```

## Folder Guide

* `notebooks/` contains Week 0 Jupyter notebooks for clinical data cleaning and visualisation.
* `docs/` contains Week 0 deliverables and Weeks 1 and 2 research proposal documents.
* `data/` is reserved for future dataset storage. The dataset is not currently included in this repository.
* `src/` is reserved for reusable Python modules and scripts that may be developed later in the program.
* `requirements.txt` lists the Python libraries needed to run the notebooks.

## Version Control Workflow

Major edits are made through a feature branch and merged into `main` using a pull request. This keeps the project history clear and supports a more reviewable workflow.

## Contributing

This repository is part of the CariSurg Healthcare AI Program coursework. Contributions are not currently expected but suggestions for improvement are welcome.

## Licence

This project is licensed under the MIT Licence. See `LICENSE` for details.

## ED Triage Workflow Diagram

```mermaid
flowchart TD

A[Patient arrival<br/>Walk-in or ambulance] --> B[Registration<br/>Clerk records demographics<br/>and presenting complaint]

B --> C[Vitals<br/>BP, HR, RR, SpO2,<br/>temperature, pain score]

C --> D[Triage nurse assessment<br/>History + vitals reviewed<br/>CTAS/acuity assigned]

D --> E{Disposition from triage<br/>or next care pathway}

E -->|Critical / unstable| F[Immediate resuscitation<br/>or urgent care area]
E -->|Needs ED assessment| G[Assigned care area<br/>or waiting area]
E -->|Likely low acuity| H[Fast track / minor care]
E -->|After ED review| I[Discharge, admit,<br/>observe, or transfer]

AI1[[AI support point 1<br/>Arrival / registration support<br/><br/>What it would do:<br/>Summarise chief complaint and arrival details<br/>so the triage nurse has a clearer starting picture.]]

AI2[[AI support point 2<br/>Vitals safety check<br/><br/>What it would do:<br/>Highlight concerning vital-sign patterns<br/>that may need faster nurse review or repeat measurement.]]

AI3[[AI support point 3<br/>End-of-triage admission-risk flag<br/><br/>What it would do:<br/>Use triage-level data to flag patients likely to need admission,<br/>supporting earlier escalation or charge nurse awareness.]]

AI4[[AI support point 4<br/>Waiting-room reassessment reminder<br/><br/>What it would do:<br/>Prompt repeat vitals or re-triage for patients with high risk,<br/>long waits, or changing symptoms.]]

AI5[[AI support point 5<br/>Handoff / bed-flow signal<br/><br/>What it would do:<br/>Carry the admission-risk flag forward to the charge nurse,<br/>clinician, or bed-planning huddle so risk is not lost in handover.]]

B -.-> AI1
C -.-> AI2
D -.-> AI3
G -.-> AI4
I -.-> AI5

C1([Constraint: disconnected records<br/>Files and patient location may not be centrally visible])
C2([Constraint: nursing workload<br/>Extra clicks or noisy alerts may be ignored])
C3([Constraint: bed-flow bottleneck<br/>Admission risk does not create inpatient beds])

AI1 -. must avoid .-> C1
AI2 -. must reduce, not add .-> C2
AI5 -. must connect to action .-> C3

classDef process fill:#ffffff,stroke:#1f4e79,stroke-width:1.5px,color:#111;
classDef decision fill:#fff8e6,stroke:#b36b00,stroke-width:1.5px,color:#111;
classDef ai fill:#eaf7fb,stroke:#008c99,stroke-width:1.5px,stroke-dasharray: 6 4,color:#111;
classDef constraint fill:#fff0f0,stroke:#b00020,stroke-width:1.5px,color:#111;

class A,B,C,D,F,G,H,I process;
class E decision;
class AI1,AI2,AI3,AI4,AI5 ai;
class C1,C2,C3 constraint;
```

**Figure 1. ED triage workflow with AI nurse-support plug-in points.**  
*Simplified from De Freitas et al.’s Caribbean ED patient-flow process and adapted for a triage-level admission prediction pilot.*

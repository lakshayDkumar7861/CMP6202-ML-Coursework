# CMP6202 Machine Learning Coursework

**Module:** CMP6202 Artificial Intelligence and Machine Learning (Birmingham City University)
**Assessment:** D2 Individual Coursework

## Project

An early-warning model for higher-education student outcomes. Using information a university has at
enrolment and by the end of a student's first semester, the project investigates whether a student's
final academic status can be predicted early enough for support to be offered.

## Research Question

> **Can we predict whether a student will drop out, remain enrolled, or graduate from their enrolment,
> demographic, socio-economic and first-semester academic data?**

## Dataset

| Field | Detail |
|---|---|
| **Name** | Predict Students' Dropout and Academic Success |
| **Source/provider** | UCI Machine Learning Repository (donated by Instituto Politécnico de Portalegre, Portugal) |
| **URL** | https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success |
| **DOI** | https://doi.org/10.24432/C5MC89 |
| **Licence** | Creative Commons Attribution 4.0 International (CC BY 4.0) |
| **Date accessed** | 22 November 2026 |
| **Academic use** | Permitted. CC BY 4.0 allows use, sharing and adaptation for any purpose, including redistribution, provided appropriate credit is given. |
| **Size** | 4,424 students × 36 features + 1 target; no missing values |

**Citation:**
Realinho, V., Vieira Martins, M., Machado, J. and Baptista, L. (2021) *Predict Students' Dropout and
Academic Success* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5MC89

The file is stored unmodified at `data/raw/data.csv` (semicolon-separated).

## Target

`Target` — a student's status at the end of the normal course duration:

| Class | Count | Share |
|---|---|---|
| Graduate | 2,209 | 49.9% |
| Dropout | 1,421 | 32.1% |
| Enrolled | 794 | 17.9% |

Task type: **multiclass classification** (imbalanced). **Dropout** is the class of primary interest, as it
is the outcome an early-warning system would act on.

## Features

36 candidate features across four groups:

- **Enrolment/application:** application mode, order and course, attendance mode, previous qualification, admission grade
- **Demographic:** marital status, nationality, gender, age at enrolment, international, displaced, special needs
- **Socio-economic:** parents' qualifications and occupations, debtor, tuition fees up to date, scholarship holder; regional unemployment, inflation and GDP
- **Academic performance:** curricular units credited/enrolled/evaluated/approved/graded for the 1st and 2nd semesters

Feature decisions, including whether 2nd-semester variables are available at the intended prediction
time (a leakage consideration), are justified in the report.

## Project Structure

```
data/raw/          Original, untouched dataset (data.csv)
data/processed/    Processed data, if a saved copy is needed
notebooks/         EDA and modelling notebooks
src/               Reusable Python functions/scripts
report/            Report drafts and final report
README.md          This file
requirements.txt   Packages required to reproduce the work
```

## Requirements

Python 3.11+ with the packages listed in `requirements.txt`.

## How to Run

1. Clone the repository: `git clone https://github.com/lakshayDkumar7861/CMP6202-ML-Coursework.git`
2. Install requirements: `pip install -r requirements.txt`
3. Open the notebooks in `notebooks/` and run them in numbered order, top to bottom.

## Models

_To be completed:_ baseline (DummyClassifier) and candidate models, compared with StratifiedKFold
cross-validation on the training set only.

## Evaluation

_To be completed:_ macro-F1, per-class precision/recall (with focus on Dropout recall), confusion matrix,
and ROC-AUC, alongside accuracy.

## Outputs

_To be completed._

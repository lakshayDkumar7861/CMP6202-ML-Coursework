"""Reusable data-loading and feature-definition helpers for the CMP6202 D2 project.

Dataset: Predict Students' Dropout and Academic Success (UCI, CC BY 4.0).
"""

from pathlib import Path

import pandas as pd

# Project root = the folder that contains data/, notebooks/, src/ ...
PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "data.csv"

TARGET = "Target"
CLASS_ORDER = ["Dropout", "Enrolled", "Graduate"]

# Typos / stray characters that exist in the original UCI column names.
COLUMN_FIXES = {
    "Nacionality": "Nationality",
}

# Columns stored as integer codes but representing UNORDERED categories.
# They must be one-hot encoded, not treated as numbers.
NOMINAL_COLS = [
    "Marital status",
    "Application mode",
    "Course",
    "Previous qualification",
    "Nationality",
    "Mother's qualification",
    "Father's qualification",
    "Mother's occupation",
    "Father's occupation",
]

# Yes/No flags already coded 0/1.
BINARY_COLS = [
    "Daytime/evening attendance",
    "Displaced",
    "Educational special needs",
    "Debtor",
    "Tuition fees up to date",
    "Gender",
    "Scholarship holder",
    "International",
]


def load_raw(path=RAW_DATA_PATH):
    """Load the untouched UCI file and tidy the column names only.

    The original file is semicolon-separated, one column name ends in a tab
    character, and 'Nationality' is misspelt. No rows or values are changed.
    """
    df = pd.read_csv(path, sep=";")
    df.columns = df.columns.str.strip()
    return df.rename(columns=COLUMN_FIXES)


def semester_cols(df, semester):
    """Return the curricular-unit columns for '1st' or '2nd' semester."""
    return [c for c in df.columns if f"{semester} sem" in c]


def numeric_cols(df):
    """Every feature that is genuinely numeric (not a coded category, flag or the target)."""
    excluded = set(NOMINAL_COLS) | set(BINARY_COLS) | {TARGET}
    return [c for c in df.columns if c not in excluded]

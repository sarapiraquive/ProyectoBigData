import re
import pandas as pd

SNAKE_RE = re.compile(r'[^a-z0-9]+')

def clean_column(col: str) -> str:
    col = col.strip().lower()
    col = SNAKE_RE.sub('_', col)
    col = re.sub(r'_+', '_', col).strip('_')
    return col

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [clean_column(c) for c in df.columns]
    return df

DATE_COLS = ["report_dat", "start_date", "end_date"]

def coerce_dates(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for c in DATE_COLS:
        if c in df.columns:
            df[c] = pd.to_datetime(df[c], errors="coerce")
    return df

def fix_ward_district(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if "ward" in df.columns:
        df["ward"] = pd.to_numeric(df["ward"], errors="coerce").fillna(-1).astype("Int64")
    if "district" in df.columns:
        df["district"] = pd.to_numeric(df["district"], errors="coerce").fillna(-1).astype("Int64")
    return df

def clean_crimes_df(df: pd.DataFrame) -> pd.DataFrame:
    df = normalize_columns(df)
    df = df.drop_duplicates()
    df = coerce_dates(df)
    df = fix_ward_district(df)
    return df

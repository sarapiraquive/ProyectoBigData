# src/io/files.py
from pathlib import Path
import pandas as pd

DATA = Path("./data")
BRONZE = DATA / "bronze"
SILVER = DATA / "silver"
GOLD   = DATA / "gold"
for d in (BRONZE, SILVER, GOLD):
    d.mkdir(parents=True, exist_ok=True)

def read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)

def write_parquet(df: pd.DataFrame, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)
    return path

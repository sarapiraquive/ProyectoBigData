from pathlib import Path
import pandas as pd
from prefect import task, get_run_logger
from dataio.files import BRONZE, SILVER, read_csv, write_parquet
from etl.clean import clean_crimes_df

@task(name="Clean CSV → Parquet (silver)")
def clean_task(csv_file: str, out_name: str = "raw_crimes_clean.parquet") -> str:
    log = get_run_logger()
    src = BRONZE / csv_file
    if not src.exists():
        raise FileNotFoundError(f"No existe: {src}")
    df = read_csv(src)
    df = clean_crimes_df(df)
    write_parquet(df, SILVER / out_name)
    log.info(f"Limpieza OK → {SILVER/out_name}  filas={len(df)}")
    return out_name

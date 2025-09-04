from prefect import task
from src.db.load import load_parquet_to_db

@task(name="Cargar Parquet (silver) → Postgres")
def load_task(parquet_name: str, table: str | None = None, if_exists: str = "replace") -> None:
    load_parquet_to_db(parquet_name, table=table, if_exists=if_exists)

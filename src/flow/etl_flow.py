from prefect import flow
from tasks.clean_task import clean_task
from tasks.load_task import load_task

@flow(name="ETL clean → parquet → Postgres")
def etl_clean_flow(csv_file: str,
                   out_parquet: str = "raw_crimes_clean.parquet",
                   table: str | None = "raw_crimes_clean"):
    clean_name = clean_task(csv_file, out_name=out_parquet)
    load_task(clean_name, table=table)
    return {"silver_parquet": clean_name, "table": table}

if __name__ == "__main__":
    # ejemplo equivalente a tu celda
    # coloca el CSV en: data/bronze/Crime_Incidents_in_2025.csv
    etl_clean_flow(csv_file="Crime_Incidents_in_2025.csv")

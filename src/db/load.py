import pandas as pd
from src.dataio.files import SILVER
from src.db.database import get_engine
from src.config.settings import settings

def load_parquet_to_db(parquet_name: str, table: str | None = None, if_exists: str = "replace") -> None:
    df = pd.read_parquet(SILVER / parquet_name)
    engine = get_engine()
    df.to_sql(table or settings.clean_table, engine, if_exists=if_exists, index=False)

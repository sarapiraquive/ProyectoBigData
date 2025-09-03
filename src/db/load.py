import pandas as pd
from ..io.files import SILVER
from .database import get_engine
from ..config.settings import settings

def load_parquet_to_db(parquet_name: str, table: str | None = None, if_exists: str = "replace") -> None:
    df = pd.read_parquet(SILVER / parquet_name)
    engine = get_engine()
    df.to_sql(table or settings.clean_table, engine, if_exists=if_exists, index=False)

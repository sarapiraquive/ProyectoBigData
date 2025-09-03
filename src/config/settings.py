from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    data_root: str = "./data"
    artifacts_dir: str = "./artifacts"
    # Postgres (ajusta usuario/host/puerto/db)
    db_url: str = "postgresql+psycopg2://postgres:psqlpass@localhost:5432/bigdatatools1"
    # tabla destino para el clean
    clean_table: str = "raw_crimes_clean"

    class Config:
        env_file = ".env"

settings = Settings()
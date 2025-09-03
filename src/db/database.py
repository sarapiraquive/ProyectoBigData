# src/db/database.py
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from config.settings import settings


def get_engine(echo: bool = False) -> Engine:
    """
    Crea el Engine de SQLAlchemy usando la URL de settings.db_url.
    Ejemplos de URL:
      - Postgres: postgresql+psycopg2://user:pass@localhost:5432/dbname
      - SQLite  : sqlite:///./artifacts/crimes.db
    """
    engine = create_engine(
        settings.db_url,
        future=True,
        echo=echo,          # ponlo True si quieres ver SQL en consola
        pool_pre_ping=True  # evita conexiones muertas
    )
    return engine


def test_connection() -> None:
    """
    Prueba una conexión simple (SELECT 1). Lanza excepción si falla.
    Útil para diagnosticar credenciales/puerto/servicio.
    """
    eng = get_engine()
    with eng.connect() as conn:
        conn.execute(text("SELECT 1"))

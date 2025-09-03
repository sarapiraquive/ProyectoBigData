from sqlalchemy import create_engine
from ..config.settings import settings

def get_engine():
    # usa psycopg2 (asegúrate de tener psycopg2-binary instalado)
    return create_engine(settings.db_url, future=True)

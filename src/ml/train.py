import pandas as pd
from sqlalchemy import create_engine
from sklearn.linear_model import LinearRegression
import pickle
from src.config.settings import settings

def train_daily_model():
    # Conexión a Postgres
    engine = create_engine(settings.db_url)

    # Query: conteo diario de crímenes
    query = """
    SELECT report_dat::date AS day, COUNT(*) AS crimes
    FROM raw_crimes_clean
    GROUP BY day
    ORDER BY day;
    """
    df = pd.read_sql(query, engine)

    # aseguramos que 'day' sea datetime
    df["day"] = pd.to_datetime(df["day"])
    df["day_num"] = (df["day"] - df["day"].min()).dt.days

    X = df[["day_num"]]
    y = df["crimes"]

    # Modelo simple
    model = LinearRegression()
    model.fit(X, y)

    # Guardar modelo entrenado
    with open("models/daily_crimes_model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Modelo entrenado y guardado en models/daily_crimes_model.pkl")

if __name__ == "__main__":
    train_daily_model()
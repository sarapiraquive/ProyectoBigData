# src/ml/evaluate.py
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib

from src.config.settings import settings


def evaluate_model(plot: bool = True) -> None:
    engine = create_engine(settings.db_url, future=True)

    query = """
    SELECT report_dat::date AS day, COUNT(*) AS crimes
    FROM raw_crimes_clean
    GROUP BY day
    ORDER BY day;
    """
    df = pd.read_sql(query, engine)

    # Asegurar datetime y generar la variable temporal
    df["day"] = pd.to_datetime(df["day"])
    df["day_num"] = (df["day"] - df["day"].min()).dt.days

    X = df[["day_num"]].values
    y = df["crimes"].values

    model = joblib.load(Path("models/daily_crimes_model.pkl"))
    y_pred = model.predict(X)

    # RMSE robusto a versiones (fallback si no existe el kw 'squared')
    try:
        rmse = mean_squared_error(y, y_pred, squared=False)
    except TypeError:
        rmse = mean_squared_error(y, y_pred) ** 0.5

    mae = mean_absolute_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    print(f"RMSE: {rmse:.3f} | MAE: {mae:.3f} | R²: {r2:.3f}")

    if plot:
        plt.figure(figsize=(12, 6))
        plt.plot(df["day"], y, label="Real")
        plt.plot(df["day"], y_pred, label="Predicho")
        plt.title("Ajuste del modelo — Crímenes diarios")
        plt.xlabel("Fecha")
        plt.ylabel("Número de crímenes")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    evaluate_model()
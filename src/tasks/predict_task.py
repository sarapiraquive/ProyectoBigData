# src/tasks/predict_task.py
from pathlib import Path
import pandas as pd
import joblib
from datetime import timedelta
from prefect import task
from sqlalchemy import create_engine
from src.config.settings import settings


@task(name="Predict Future Crimes")
def predict_future_crimes(days: int = 10) -> pd.DataFrame:
    """
    Genera predicciones de crímenes para un número de días futuros
    usando el modelo entrenado.
    """
    model_path = Path("models/daily_crimes_model.pkl")
    if not model_path.exists():
        raise FileNotFoundError(f"Modelo no encontrado en {model_path}")

    model = joblib.load(model_path)

    # Fechas futuras
    last_date = pd.Timestamp.today().normalize()
    future_days = pd.date_range(start=last_date + timedelta(days=1),
                                periods=days, freq="D")

    # Convertir fechas a feature numérica
    min_date = pd.Timestamp("2025-01-01")  # Ajusta al dataset real
    X_future = (future_days - min_date).days.values.reshape(-1, 1)

    preds = model.predict(X_future)

    df_pred = pd.DataFrame({
        "day": future_days,
        "pred_crimes": preds
    })

    return df_pred


@task(name="Save Predictions to Postgres")
def save_predictions_to_db(df_pred: pd.DataFrame):
    """
    Guarda las predicciones en Postgres en la tabla `predicted_crimes`.
    """
    engine = create_engine(settings.db_url)

    df_pred.to_sql(
        "predicted_crimes",
        engine,
        if_exists="replace",  # usa "append" si quieres acumular
        index=False
    )

    print("Predicciones guardadas en Postgres (tabla: predicted_crimes)")
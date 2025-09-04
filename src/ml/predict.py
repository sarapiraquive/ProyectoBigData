import pickle
import pandas as pd
from datetime import timedelta
from sqlalchemy import create_engine
from src.config.settings import settings

def predict_future(days_ahead=7):
    # Cargar modelo entrenado
    with open("models/daily_crimes_model.pkl", "rb") as f:
        model = pickle.load(f)

    # Conectar a la BD y obtener la última fecha
    engine = create_engine(settings.db_url)
    query = "SELECT MAX(report_dat::date) as last_day FROM raw_crimes_clean;"
    last_day = pd.read_sql(query, engine)["last_day"].iloc[0]

    # Generar días futuros
    future_days = pd.date_range(last_day + timedelta(days=1), periods=days_ahead)

    # Convertir a feature numérica
    day_num_start = (future_days[0] - pd.to_datetime("2025-01-01")).days
    future_df = pd.DataFrame({
        "day": future_days,
        "day_num": [(d - pd.to_datetime("2025-01-01")).days for d in future_days]
    })

    # Predicciones
    future_df["pred_crimes"] = model.predict(future_df[["day_num"]])

    print("🔮 Predicciones de crímenes futuros:")
    print(future_df[["day", "pred_crimes"]])

    return future_df

if __name__ == "__main__":
    predict_future(days_ahead=10)
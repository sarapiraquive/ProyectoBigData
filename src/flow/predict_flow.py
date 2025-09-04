from prefect import flow
from src.tasks.predict_task import predict_future_crimes, save_predictions_to_db


@flow(name="Crime Prediction Flow")
def run_prediction_flow(days: int = 10):
    df_pred = predict_future_crimes(days)
    save_predictions_to_db(df_pred)
    print("Predicciones generadas y guardadas en Postgres:")
    print(df_pred.head())


if __name__ == "__main__":
    run_prediction_flow(days=15)
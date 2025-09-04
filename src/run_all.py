import subprocess
import psycopg2

def run_step(name, command):
    print(f"\nEjecutando paso: {name}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error en el paso: {name}")
        print(e.stderr)
        exit(1)

def verify_table_count(table_name, db="bigdatatools1", user="psqluser", password="psqlpass", host="localhost", port=5432):
    try:
        conn = psycopg2.connect(
            dbname=db,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM {table_name};")
        count = cur.fetchone()[0]
        print(f"Verificación: la tabla '{table_name}' tiene {count} registros")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error verificando {table_name}: {e}")

if __name__ == "__main__":
    # ETL
    run_step("Limpieza y carga de datos (ETL)", "python -m src.flow.etl_flow")
    verify_table_count("raw_crimes_clean")

    # Entrenamiento del modelo
    run_step("Entrenamiento del modelo", "python -m src.ml.train")
    run_step("Evaluación del modelo", "python -m src.ml.evaluate")

    # Predicciones
    run_step("Predicciones y guardado en Postgres", "python -m src.flow.predict_flow")
    verify_table_count("predicted_crimes")

    # Analytics
    run_step("Consultas de analytics", "python -m src.analytics.queries")
    run_step("Generación de gráficos", "python -m src.analytics.plots")
    run_step("Generación de reportes", "python -m src.analytics.reports")

    print("\nPipeline ejecutado con éxito de principio a fin")
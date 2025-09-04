import pandas as pd
from sqlalchemy import text
from src.db.database import get_engine
from src.analytics import queries
from src.analytics import plots

def run_report(query, plot_func, *args, **kwargs):
    """Ejecuta query y manda dataframe al gráfico"""
    engine = get_engine()
    with engine.connect() as conn:
        df = pd.read_sql(text(query), conn)
    plot_func(df, *args, **kwargs)

if __name__ == "__main__":
    # 1. Crímenes diarios
    run_report(queries.daily_crimes_query, plots.plot_daily_crimes)

    # 2. Mapa de crímenes
    run_report(queries.map_sample_query, plots.plot_map, output_file="mapa_crimenes.html")

    # 3. Top wards
    run_report(queries.wards_query, plots.plot_top_wards)

    # 4. Delitos más comunes
    run_report(queries.offense_query, plots.plot_top_offenses)

    # 5. Distribución por turno
    run_report(queries.shift_query, plots.plot_shift_distribution)
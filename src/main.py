# main.py (en la raíz del repo)
import os, sys

# agrega ./src al sys.path para que "flow", "tasks", etc. sean importables
HERE = os.path.dirname(__file__)
SRC = os.path.join(HERE, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from flow.etl_flow import etl_clean_flow  # importa tu flow

if __name__ == "__main__":
    # nombre del CSV que está en data/bronze/
    etl_clean_flow(csv_file="Crime_Incidents_in_2025.csv")

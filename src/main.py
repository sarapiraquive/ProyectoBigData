

from ProyectoBigData.src.flow.main_flow import crime_data_ingestion_pipeline

if __name__ == "__main__":
    result = crime_data_ingestion_pipeline()
    print("Pipeline ejecutado exitosamente!")
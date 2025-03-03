from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.data_ingestion import DataIngestion
from src.cnnClassifier.logging import logger

STAGE_NAME="Data_ingestion_stage"

class DataingestiontrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingetion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__=="__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started<<<<<<")
        obj=DataingestiontrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
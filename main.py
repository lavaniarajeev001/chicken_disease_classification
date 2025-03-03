from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataingestiontrainingPipeline
from src.cnnClassifier.logging import logger

STAGE_NAME="Data_ingestion_stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started<<<<<<")
    obj=DataingestiontrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
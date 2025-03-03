from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataingestiontrainingPipeline
from src.cnnClassifier.logging import logger
from src.cnnClassifier.pipeline.stage_02_data_preparebasemodel import PrepareBaseModelTrainingPipeline

STAGE_NAME="Data_ingestion_stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started<<<<<<")
    obj=DataingestiontrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

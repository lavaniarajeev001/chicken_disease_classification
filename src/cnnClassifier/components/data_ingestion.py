import os
import urllib.request as request
import zipfile
from src.cnnClassifier.logging import logger
from src.cnnClassifier.utils.common import get_size
from src.cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config=config
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers=request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded")
        else:
            logger.info(f"{self.config.local_data_file} already exists")

    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
            zip_ref.extractall(unzip_path)
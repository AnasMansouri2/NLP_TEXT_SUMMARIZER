import os

os.chdir("../")


from dataclasses import dataclass
from pathlib import Path
import os
import urllib.request as request
import zipfile
from NLP_TEXT_SUMMARIZER.logging import logger
from NLP_TEXT_SUMMARIZER.utils.common import get_size
from NLP_TEXT_SUMMARIZER.constants import *
from NLP_TEXT_SUMMARIZER.utils.common import read_yaml, create_directories

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """Récupère la configuration pour l'ingestion des données"""

        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_file(self):
        """Télécharge le fichier si ce dernier n'existe pas déjà"""

        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} téléchargé avec succès avec les informations suivantes : \n{headers}")
        else:
            logger.info(f"Le fichier existe déjà avec une taille de : {get_size(Path(self.config.local_data_file))}")  

        
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extrait le fichier zip dans le répertoire de données
        La fonction ne retourne rien
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

try:
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.extract_zip_file()
except Exception as e:
    raise e

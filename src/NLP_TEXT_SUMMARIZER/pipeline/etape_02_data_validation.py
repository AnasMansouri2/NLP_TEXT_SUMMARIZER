from NLP_TEXT_SUMMARIZER.config.configuration import ConfigurationManager
from NLP_TEXT_SUMMARIZER.conponents.data_validation import DataValiadtion
from NLP_TEXT_SUMMARIZER.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_files_exist()
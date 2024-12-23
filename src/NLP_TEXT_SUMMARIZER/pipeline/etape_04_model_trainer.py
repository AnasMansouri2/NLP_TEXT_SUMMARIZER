from NLP_TEXT_SUMMARIZER.config.configuration import ConfigurationManager
from NLP_TEXT_SUMMARIZER.components.model_trainer import ModelTrainer
from NLP_TEXT_SUMMARIZER.logging import logger


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
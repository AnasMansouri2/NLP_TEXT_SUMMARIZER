import logging

# Créez un logger pour le projet NLP_TEXT_SUMMARIZER
logger = logging.getLogger("NLP_TEXT_SUMMARIZER")
logger.setLevel(logging.INFO)

# Créez un handler pour afficher les messages dans la console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Définissez un format de log
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Ajoutez le handler au logger
logger.addHandler(console_handler)

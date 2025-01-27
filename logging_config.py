import logging.config
import json

def setup_logging():
    with open('logging_config.json', 'r') as file:
        logging_config = json.load(file)
    logging.config.dictConfig(logging_config)

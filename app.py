import logging
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

class Sag:
    @staticmethod
    def debug(nachricht):
        logger.debug(nachricht)

    @staticmethod
    def info(nachricht):
        logger.info(nachricht)

    @staticmethod
    def warning(nachricht):
        logger.warning(nachricht)

    @staticmethod
    def error(nachricht):
        logger.error(nachricht)

    @staticmethod
    def critical(nachricht):
        logger.critical(nachricht)

def main():
    Sag.debug('Debug level log')
    Sag.info('Info level log')
    Sag.warning('Warning level log')
    Sag.error('Error level log')
    Sag.critical('Critical level log')

if __name__ == '__main__':
    main()

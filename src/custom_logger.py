import logging
import sys

def get_custom_logger(logger_name):
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s -- %(levelname)s -- %(message)s')
    logger = logging.getLogger(logger_name)

    return logger

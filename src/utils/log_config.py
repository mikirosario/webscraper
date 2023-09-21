import logging
from logging.handlers import RotatingFileHandler
from src.constants import LOG_FILE_NAME, LOG_FILE_MAX_BYTES, LOG_FILE_MAX_NUM

def setup_logger(name):
    # Set up the logger
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Create a console handler to log messages to the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # Try to create a rotating file handler to log messages to a file
        try:
            file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=LOG_FILE_MAX_BYTES, backupCount=LOG_FILE_MAX_NUM)
            file_handler.setLevel(logging.WARNING)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except PermissionError:
            logger.error("Permission denied: Unable to write to the log file.", exc_info=1)
        except OSError:
            logger.error("OS error (e.g., disk full): Failed to create or write to the log file.", exc_info=1)
        except Exception as e:
            logger.error(f"Unexpected error with the log file: {e}", exc_info=1)

    return logger
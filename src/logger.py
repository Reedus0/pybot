import logging
import os

def init_logging():
    log_path = os.getcwd() + os.getenv("LOG_PATH")
    log_name = os.getenv("LOG_FILE_NAME")

    if not os.path.exists(log_path):
        os.makedirs(log_path)

    logging.basicConfig(
        filename=log_path + log_name, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )

    logging.getLogger(__name__)

    log("Initiated logger!")

def log(data):
    logging.info(data)
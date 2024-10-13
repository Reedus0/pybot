import logging
import os

def init_logging():
    log_path = "/logs/"
    log_name = "bot.log"

    if not os.path.exists(log_path):
        os.makedirs(log_path, 0o777)

    logging.basicConfig(
        filename=log_path + log_name, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )

    logging.getLogger(__name__)

    log("Initiated logger!")

def log(data):
    logging.info(data)
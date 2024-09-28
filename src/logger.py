import logging

def init_logging():
    logging.basicConfig(
        filename="../logfile.txt", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )

    logging.getLogger(__name__)
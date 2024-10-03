import re
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv

from logger import *
from bot import *
from ssh import *
from sql import *
from handlers import *

def main():

    load_dotenv()

    # init_logging()
    # init_ssh()
    # init_sql()

    init_bot()
    simple_handlers = init_simple_handlers()
    complex_handlers = init_complex_handlers()

    bot_add_simple_handlers(simple_handlers)
    bot_add_complex_handlers(complex_handlers)
    bot_listen()

    return 0

if __name__ == "__main__":
    main()
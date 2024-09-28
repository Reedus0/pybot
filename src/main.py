
import re
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv

from logger import *
from bot import *
from ssh import *
from handlers import *

def main():

    load_dotenv()

    init_logging()
    init_ssh()

    bot = init_bot()
    simple_handlers = init_simple_handlers()
    complex_handlers = init_complex_handlers()

    bot_add_simple_handlers(bot, simple_handlers)
    bot_add_complex_handlers(bot, complex_handlers)
    bot_listen(bot)

    return 0

if __name__ == "__main__":
    main()
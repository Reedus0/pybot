from logger import *
from bot import *

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
import re
import os

def start(update, context):
    user = update.effective_user
    update.message.reply_text(f'Привет {user.full_name}!')

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():

    load_dotenv()

    TOKEN = os.getenv("TOKEN")

    init_logging()

    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
		
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
		
    updater.start_polling()
    updater.idle()

    return 0

if __name__ == "__main__":
    main()
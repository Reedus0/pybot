import os
from telegram.ext import Updater, CommandHandler, CommandHandler, MessageHandler, Filters, ConversationHandler

from logger import *

def init_bot():

    bot_token = os.getenv("TOKEN")
    bot = Updater(bot_token, use_context=True)

    log("Initiated bot!")

    return bot
    
def send_message(update, message):
    message_length = len(message) 
    for i in range(int(message_length / 4096) + 1):
        update.message.reply_text(message[i * 4096 : (i + 1) * 4096])

def bot_add_simple_handlers(bot, handlers):
    dp = bot.dispatcher

    for handler_name in handlers.keys(): 
        dp.add_handler(CommandHandler(handler_name, handlers[handler_name]))

    log("Added simple handlers!")


def bot_add_complex_handlers(bot, handlers):
    dp = bot.dispatcher

    for handler in handlers.keys(): 
        states = {}

        for state in handlers[handler][1].keys():
            states[state] = [MessageHandler(Filters.text & ~Filters.command, handlers[handler][1][state])]

        dp.add_handler(ConversationHandler(
        entry_points=[CommandHandler(handler, handlers[handler][0])],
        states=states,
        fallbacks=[]
    ))

    log("Added complex handlers!")

def bot_listen(updater):
    log("Bot is listening!")

    updater.start_polling()
    updater.idle()
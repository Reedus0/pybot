import re

from telegram.ext import CommandHandler, MessageHandler, Filters, ConversationHandler

from ssh import *
from sql import *
from bot import *

context_data = None

def get_release(update, context):
    result = ssh_do("uname -a")
    send_message(update, result)

def get_uname(update, context):
    result = "Hostname: " + ssh_do("hostname")
    result += "CPU: " + ssh_do("lscpu")
    result += "uname: " + ssh_do("uname -a")
    send_message(update, result)

def get_uptime(update, context):
    result = ssh_do("uptime")
    send_message(update, result)

def get_df(update, context):
    result = ssh_do("df -h")
    send_message(update, result)

def get_df(update, context):
    result = ssh_do("df -h")
    send_message(update, result)

def get_free(update, context):
    result = ssh_do("cat /proc/meminfo")
    send_message(update, result)

def get_mpstat(update, context):
    result = ssh_do("vmstat")
    send_message(update, result)

def get_w(update, context):
    result = ssh_do("w")
    send_message(update, result)

def get_auths(update, context):
    result = ssh_do("cat /var/log/auth.log | tail -n 10")
    print(result)
    send_message(update, result)

def get_critical(update, context):
    result = ssh_do("cat /var/log/faillog | tail -n 5")
    send_message(update, result)

def get_ps(update, context):
    result = ssh_do("ps -ef")
    send_message(update, result)

def get_ss(update, context):
    result = ssh_do("ss")
    send_message(update, result)

def get_apt_list(update, context):
    args = update.message.text.split(" ")

    result = ssh_do("apt list")
    if (len(args) > 1):
        result = ssh_do("apt show " + args[1])
    send_message(update, result)

def get_services(update, context):
    result = ssh_do("systemctl")
    send_message(update, result)

def get_repl_logs(update, context):
    with open("./logs/postgresql.log", "r") as file:
        result = file.read()
        send_message(update, result[-500:])
        file.close()

def get_emails(update, context):
    result = sql_do("SELECT email FROM email;")
    if (len(result) == 0):
        send_message(update, "Адреса не найдены")
        return
    result = [x[0] for x in result]
    result = "\n".join(result)
    send_message(update, result)

def get_phone_numbers(update, context):
    result = sql_do("SELECT phone FROM phone;")
    if (len(result) == 0):
        send_message(update, "Телефоны не найдены")
        return
    result = [x[0] for x in result]
    result = "\n".join(result)
    send_message(update, result)

def verify_password(update, context):
    send_message(update, "Введите пароль:")

    return "get_password"

def get_password(update, context):
    password = update.message.text
    result = 1

    if (len(password) < 8): result = 0
    if (not re.search("[A-Z]", password)): result = 0
    if (not re.search("[a-z]", password)): result = 0
    if (not re.search("[0-9]", password)): result = 0
    if (not re.search("[!@#$%^&*()]", password)): result = 0

    send_message(update, "Пароль сложный" if result else "Пароль простой")

    return ConversationHandler.END

def find_email(update, context):
    send_message(update, "Введите текст:")

    return "get_email"

def get_email(update, context):
    global context_data
    text = update.message.text

    result = re.findall(r"[\w]+@[\w]+\.[\w]{2,4}", text)

    if (not result):
        send_message(update, "Адреса не найдены")
        return ConversationHandler.END

    send_message(update, "\n".join(result))

    context_data = result

    send_message(update, "Добавить в базу данных? (Да/Нет)")
    return "add_email"

def add_email(update, context):
    text = update.message.text
    if (text == "Да"):
        sql_do(f"INSERT INTO email(email) VALUES ('" + "'),('".join(context_data) + "');");
        send_message(update, "Данные добавлены")
    else:
        send_message(update, "Данные не были добавлены")
    return ConversationHandler.END

def find_phone(update, context):
    send_message(update, "Введите текст:")

    return "get_phone"

def get_phone(update, context):
    global context_data
    text = update.message.text

    result = re.findall(r"\+?[78]{1}[\s(-]{1,2}[\d]{3}[\s)-]{1,2}[\d]{3}[\s)-]?[\d]{2}[\s)-]?[\d]{2}", text)

    if (not result):
        send_message(update, "Телефоны не найдены")
        return ConversationHandler.END

    send_message(update, "\n".join(result))

    context_data = result

    send_message(update, "Добавить в базу данных? (Да/Нет)")
    return "add_phone"

def add_phone(update, context):
    text = update.message.text
    if (text == "Да"):
        sql_do(f"INSERT INTO email(email) VALUES ('" + "'),('".join(context_data) + "');");
        send_message(update, "Данные добавлены")
    else:
        send_message(update, "Данные не были добавлены")
    return ConversationHandler.END

def init_simple_handlers():
    handlers = {}

    handlers["get_release"] = get_release
    handlers["get_uname"] = get_uname
    handlers["get_uptime"] = get_uptime
    handlers["get_df"] = get_df
    handlers["get_free"] = get_free
    handlers["get_mpstat"] = get_mpstat
    handlers["get_w"] = get_w
    handlers["get_auths"] = get_auths
    handlers["get_critical"] = get_critical
    handlers["get_ps"] = get_ps 
    handlers["get_ss"] = get_ss 
    handlers["get_apt_list"] = get_apt_list 
    handlers["get_services"] = get_services 
    handlers["get_repl_logs"] = get_repl_logs 
    handlers["get_emails"] = get_emails 
    handlers["get_phone_numbers"] = get_phone_numbers 

    log("Initiated simple handlers!")

    return handlers


def init_complex_handlers():
    handlers = {}

    handlers['verify_password'] = [verify_password, {"get_password": get_password}]
    handlers['find_email'] = [find_email, {"get_email": get_email, "add_email": add_email}]
    handlers['find_phone'] = [find_phone, {"get_phone": get_phone, "add_phone": add_phone}]

    log("Initiated complex handlers!")

    return handlers
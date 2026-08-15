import logging
import os

from dotenv import load_dotenv
import telebot
from telebot.types import Message
import random

from facts import facts
from history import check_fact_is_shown, save_fact_as_showed

load_dotenv()

logger = telebot.logger

is_debug = os.getenv("DEBUG_MODE") == "True"
if is_debug:
    telebot.logger.setLevel(logging.DEBUG)

token = os.getenv("BOT_TOKEN", "")
bot = telebot.TeleBot(token, colorful_logs=True)


@bot.message_handler(commands=["start"])
def send_welcome(message: Message):
    bot.send_message(
        message.chat.id,
        "Приветствую тебя, человек!\nЯ знаю много интересного о слизнях.\nНапиши /fact в чат, чтобы я поделился своей мудростью!",
    )


@bot.message_handler(commands=["fact"])
def send_fact(message: Message):
    chat_id = message.chat.id

    fact = None
    while True:
        fact_index = random.randint(0, len(facts) - 1)
        fact = facts[fact_index]
        if not check_fact_is_shown(chat_id, fact):
            break

    bot.send_message(chat_id, fact)
    save_fact_as_showed(chat_id, fact)


@bot.message_handler(content_types=["new_chat_members"])
def handle_add_to_chat(message: Message):
    if message.new_chat_members != None and bot.bot_id in [
        m.id for m in message.new_chat_members
    ]:
        bot.send_message(
            message.chat.id,
            "Приветствую вас, двуногие!\nЯ мудрый слизень, знаю всё о своём народе.\nПишите /fact в чат, чтобы я поделился своей мудростью!",
        )


bot.infinity_polling()

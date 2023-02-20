from aiogram import Bot, Dispatcher, types
import logging
import sqlite3
from config import telegram_bot_token


conn = sqlite3.connect('databases/data.db')
cur = conn.cursor()

bot = Bot(token=telegram_bot_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
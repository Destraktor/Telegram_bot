from aiogram import *
from create_bot import dp
from handlers import start

start.register_handlers_start(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, fast=True)
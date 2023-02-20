from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

MainMenu = InlineKeyboardMarkup(row_width=1)

menu = InlineKeyboardButton(text="Main Menu", callback_data="MainMenu")
MainMenu.insert(menu)
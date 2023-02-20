from aiogram import types, Dispatcher
from create_bot import cur, conn, bot, dp
import handlers.markups as nav

@dp.callback_query_handler(text="MainMenu")
async def start(message: types.Message):
    tg_id = message.from_user.id
    info = cur.execute("select * from users_info where tg_id = ?", (tg_id,))
    if info.fetchone() is None:
        tg_teg = message.from_user.username
        tg_fullname = message.from_user.full_name
        date_join = message.date
        date_join_month = 0
        date_join_day = 0

        if 0 < date_join.month < 10:
            date_join_month = "0{0}".format(date_join.month)
        elif date_join.month > 9:
            date_join_month = date_join.month
            # check for a single-count month

        if 0 < date_join.day < 10:
            date_join_day = "0{0}".format(date_join.day)
        elif date_join.day > 9:
            date_join_day = date_join.day
            # check for a single day
            # I'm too lazy to prescribe for seconds, minutes, hours

        date_join = "{0}:{1}:{2} {3}.{4}.{5}".format(date_join.hour,
                                                     date_join.minute,
                                                     date_join.second,
                                                     date_join_day,
                                                     date_join_month,
                                                     date_join.year)

        val = [(tg_id, tg_teg, tg_fullname, date_join)]
        cur.executemany("INSERT INTO users_info VALUES (?, ?, ?, ?)", val)
        conn.commit()

        await bot.send_message(tg_id,
                               "<i> Authorization passed </i>",
                               reply_markup=nav.MainMenu)

    await bot.send_message(tg_id,
                           "<b> Main Menu </b>",
                           reply_markup=nav.MainMenu)


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
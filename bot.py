
"""

This is a echo bot.

It echoes any incoming text messages.

"""

import logging
from aiogram import Bot, Dispatcher, executor, types
import psycopg2
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_hi = KeyboardButton('/cities')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)

API_TOKEN = '5827061682:AAH1adrHvjSmvkoNke_Z2Y3gzYohP68Si9c'

conn = psycopg2.connect(
    database="cities",
    user="postgres",
    password='1',
    host='127.0.0.1',
    port='5432')
cur = conn.cursor()

# Configure logging

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.", reply_markup=greet_kb)

@dp.message_handler(commands=['end'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    greet_kb = ReplyKeyboardRemove()
    await message.reply("HI!", reply_markup=greet_kb)


@dp.message_handler(commands=['cities'])
async def echo(message: types.Message):
    cur.execute('select * from city;')
    for i in cur.fetchall():
        print(i[0])
        await message.answer_photo(caption=f'Город - {i[1]}\n',photo=i[2])


@dp.message_handler()
async def echo(message: types.Message):
    if (gen:=message.text.split('\n'))[0]=='Добавить':
        cur.execute(f"insert into city(title, photo) values('{gen[1]}',  '{gen[2]}');")
        conn.commit()
        await message.answer("Город добавлен")
    else:
        try:
            cur.execute(f'select * from city where id={message.text}')
            i = cur.fetchall()[0]
            await message.answer_photo(caption=f'Город - {i[1]}\n', photo=i[2])
        except:
            await message.answer("Извините, такого корода нет!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)1
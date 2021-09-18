from flask import Blueprint, render_template

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import os


handler = Blueprint('handler', __name__, template_folder='templates')

# telegram_token = os.environ.get('TELEGRAM_TOKEN')
bot = Bot(token=os.environ.get('TELEGRAM_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@handler.route('/')
def index():
    # print(os.environ.get('TELEGRAM_TOKEN'))
    return render_template('telegram/index.html', title='Telegram Blueprint title')



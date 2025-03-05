import datetime
import json
import random

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from bd.operations import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, file, File

from create_bot import dp, bot
from keyboards import kb_service, kb_country


async def start_country(message: types.Message):
    await bot.send_message(message.chat.id, f'Выберите пунк меню', reply_markup=kb_country)


async def change_country(message: types.Message):

    idLs = findIdLsIdTelegram(message.from_user.id)
    sorted(idLs, key=lambda item: item['id'], reverse=True)

    kb_count = InlineKeyboardMarkup(resize_keyboard=False, one_time_keyboard=True)

    for i in idLs:
        count: int = 0

        await bot.send_message(message.chat.id,
                               f"Адрес: {i['address'][0]['city']}, "
                               f"{i['address'][0]['street']}, "
                               f"д. {i['address'][0]['house']}, кв, {i['address'][0]['apartment']}")

        counter = sorted(i['counters'], key=lambda item: item['id'], reverse=True)

        for j in counter:

            count = count + 1

            if datetime.datetime.strptime(j['data_verification'], '%d.%m.%Y') > datetime.datetime.now():

                bi = InlineKeyboardButton(text="Передать показания", callback_data=f'id_{j["id"]}')
                kb_count.inline_keyboard.clear()
                kb_count.add(bi)

                await bot.send_message(message.chat.id,
                                       F"Счетчик № {count} {j['name_counter']}\n"
                                       F"Текущие показания: {j['current_indications']}\n"
                                       F"Новые новые показания: {j['new_indications']}\n"
                                       F"Дата поверки:  {j['data_verification']}",
                                       reply_markup=kb_count)
            else:
                bi = InlineKeyboardButton(text="Передать информацию о поверке", callback_data=f'id_{j["id"]}')
                kb_count.inline_keyboard.clear()
                kb_count.add(bi)

                await bot.send_message(message.chat.id,
                                       F"Счетчик № {count} {j['name_counter']}\n"
                                       F"Текущие показания: {j['current_indications']}\n"
                                       F"Новые новые показания: {j['new_indications']}\n"
                                       F"Дата поверки:  {j['data_verification']}",
                                       reply_markup=kb_count)

    #await bot.send_message(message.chat.id, f'У вас {len(idLs)} счетчика горячей воды', reply_markup=kb_count)


def show_counter_handler(dp: Dispatcher):
    dp.register_message_handler(start_country, commands=['Счетчики', 'counter'], state=None)
    dp.register_message_handler(change_country, commands=['Показания'], state=None)
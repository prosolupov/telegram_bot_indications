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


class FSMReplacementCountry(StatesGroup):

    replacement_country_start = State()
    phone = State()
    email = State()
    akt_foto_country = State()
    passport_foto_country = State()
    certificate_foto_country = State()
    finish_replacement_country = State()


user_request = {}
list_foto = {}


# Расчет по приборам учета после установки(вновь)
async def replacement_country_start(message: types.Message):
    await FSMReplacementCountry.replacement_country_start.set()
    await bot.send_message(message.chat.id, f'Введите ФИО')
    user_request["id_user"] = message.from_user.id
    user_request["name_request"] = message.text


async def replacement_country_fio(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
        user_request["fio"] = message.text
    await FSMReplacementCountry.next()
    await bot.send_message(message.chat.id, f'Введите номер телефона')


async def replacement_country_phone(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['emai'] = message.text
        user_request["phone"] = message.text
    await FSMReplacementCountry.next()
    await bot.send_message(message.chat.id, f'Введите адрес электронной почты')


async def replacement_country_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['emai'] = message.text
        user_request["emai"] = message.text
    await FSMReplacementCountry.next()
    await bot.send_message(message.chat.id, f'Загрузите акт ввода в эксплуатацию')


# async def select_photo_country(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['akt_foto_country'] = message.text
#         user_request["email"] = message.text
#     await FSMReplacementCountry.next()
#     await bot.send_message(message.chat.id, f'Загрузите акт ввода в эксплуатацию')


async def akt_photo_country(message: types.Message, state: FSMContext):
    id_photo = message.photo[-1].file_id
    async with state.proxy() as data:
        data["akt_foto_country"] = message.photo[-1].file_id
        user_request["email"] = message.text
        list_foto["akt"] = id_photo
    await FSMReplacementCountry.next()
    await bot.send_message(message.chat.id, f'Загрузите паспорт ИПУ')


async def passport_photo_country(message: types.Message, state: FSMContext):
    id_photo = message.photo[-1].file_id
    async with state.proxy() as data:
        data["passport_foto_country"] = message.photo[-1].file_id
        list_foto["passport"] = id_photo
    await FSMReplacementCountry.next()
    await bot.send_message(message.chat.id, f'Свидетельство о поверке ИПУ')


async def certificate_photo_country(message: types.Message, state: FSMContext):
    id_photo = message.photo[-1].file_id
    async with state.proxy() as data:
        data["certificate_foto_country"] = message.photo[-1].file_id
        list_foto["certificate"] = id_photo
        user_request["list_foto"] = list_foto
    await state.finish()
    number_request = userRequest(user_request)
    # sent_email_request(message, user_request)

    await message.reply(f'Спасибо, номер вашего обращения {number_request}')


async def echo(message: types.Message):
    await bot.send_message("1997786279", "Квитанция")
    await bot.send_document("5004543057", open('Квитанция.pdf', 'rb'))


def new_setup_counter_handler(dp: Dispatcher):
    dp.register_message_handler(replacement_country_start, commands=['Смена_счетчика'], state=None)
    dp.register_message_handler(replacement_country_fio, state=FSMReplacementCountry.replacement_country_start)
    dp.register_message_handler(replacement_country_phone, state=FSMReplacementCountry.phone)
    dp.register_message_handler(replacement_country_email, state=FSMReplacementCountry.email)
    dp.register_message_handler(akt_photo_country, content_types=['photo'], state=FSMReplacementCountry.akt_foto_country)
    dp.register_message_handler(passport_photo_country, content_types=['photo'], state=FSMReplacementCountry.passport_foto_country)
    dp.register_message_handler(certificate_photo_country, content_types=['photo'], state=FSMReplacementCountry.certificate_foto_country)
    # dp.register_message_handler(finish_replacement_country, state=FSMReplacementCountry.load_foto_country)
    # dp.register_message_handler(echo, commands=['Начисление'], state=None)
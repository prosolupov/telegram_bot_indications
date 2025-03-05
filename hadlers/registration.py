import re

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from bd.operations import *

from create_bot import dp, bot
from keyboards import kb_service


class FSMRegistration(StatesGroup):
    registration = State()
    ls = State()


async def start_registration(message: types.Message):
    await FSMRegistration.registration.set()
    await bot.send_photo(message.chat.id,
                         open('kv.jpg', 'rb'),
                         'Введите свой номер лицевого счета. Он написан у вас в квитанции')


async def ls_registration(message: types.Message, state=FSMContext):

    if bool(re.compile('^554(\d{10})$').match(message.text)):
        idLs = getIdLs(int(message.text))
    else:
        await message.reply("К сожалению вы неверно указали лицевой счет.")

    if idLs != 0:

        setIdUserTelegram(int(message.text), message.from_user.id)
        await message.reply("Лицевой счет зарегистрирован")
        await bot.send_message(message.chat.id, f'Выберите пунк меню', reply_markup=kb_service)
        await state.finish()
    else:
        await message.reply("Лицевой счет указан не верно.")
        await message.reply("Введите лицевой счёт из 13 чисел.")


def register_handler_registration(dp: Dispatcher):
    dp.register_message_handler(start_registration, commands=['Регистрация'], state=None)
    dp.register_message_handler(ls_registration, state=FSMRegistration.registration)

import json

from aiogram import types, Dispatcher

from bd.operations import getPayment
from create_bot import dp, bot
from keyboards import kb_service, kb_calculation


async def show_calculation_menu(message: types.Message):
    await bot.send_message(message.chat.id, f'Выберите пунк меню', reply_markup=kb_calculation)


async def show_calculation(message: types.Message):
    data = getPayment(message.from_user.id).content
    calculation = json.loads(data)
    await bot.send_message(message.chat.id, "Сумма задолженности по состоянию на 09.10.2023\n"
                                            f"К оплате за месяц: {calculation[0]['sum_to_pay']}\n"
                                            f"С учетом долга: {calculation[0]['debt_end']}")


def show_calculation_handler(dp: Dispatcher):
    dp.register_message_handler(show_calculation_menu, commands=['Начисления', 'calculation'], state=None)
    dp.register_message_handler(show_calculation, commands=['Задолженность'], state=None)
import requests
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram import types, Dispatcher
from bd.operations import *
from keyboards import kb_registration, kb_service
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from create_bot import dp, bot


async def command_start(message: types.Message):
    idLs = findIdLsIdTelegram(message.from_user.id)
    if len(idLs) == 0:
        await bot.send_message(message.chat.id, f'Здравствуйте! \nЗарегистрируйте лицевой счет. '
                                                f'\nДля регистрации нажмите кнопку Регистрация',
                               reply_markup=kb_registration)
    else:
        await bot.send_message(message.chat.id, f'Выберите пунк меню', reply_markup=kb_service)


async def comand_send(message: types.Message):
    id_user = [5441008992, 1787174203, 1063643914, 5317025622, 5281486289, 6585069716, 280781653, 6306913347, 5183323965,
               723682027, 978278892, 5161032769, 644665186, 6982211201, 1702639654, 1437043702, 5218441762, 504137396,
               543301726, 289545985, 5521425266, 1731621890, 6629523585, 2118011222, 6803987197, 5020219631, 5680790556,
               6632145081, 2022344917, 693522710, 5865144068, 1854397739, 5243743255, 6915382039, 5614661454, 1835835898,
               5367191676, 5244079205, 1224930269, 2020473458, 2020473458, 1235000477, 6316891073, 334184177, 5222581393,
               6174070856, 1498538274, 6747263662, 6810193290, 5014035446, 5090315321, 5438448616, 1264135799, 2113738854,
               814921742, 1379495996, 5265223644, 1064282530, 959622876, 1014813098, 574445788, 5308140110, 514397171,
               1889994595, 210730280, 6408437885, 114836450, 1726855039, 833132482, 6914934022, 5015063075, 5221669072,
               1975951507, 1473276742, 1473276742, 5968297714, 1044184557, 5981583213, 2139035791, 795515158, 5000482661,
               1387745775, 5105243699, 910951257, 5852958871, 6145220649, 5220330947, 5092622819, 5628851520, 7102518721,
               849808203, 574103134, 973252476, 6183039565, 5625999959, 769231779, 1028847286, 5497229909, 5497229909, 6424462582,
               5288555869, 2072400353, 1459459222, 726883096, 764496079, 942629761, 950324879, 1480522354, 515375218,
               1470749857, 480986346, 512764968, 232959786, 6691327346, 1322263292, 5264911227, 832861707, 5328356343,
               7338303079, 6193728187, 5130836027, 85883988]

    for id in id_user:
        try:
            await bot.send_message(id, 'Здравствуйте! Буду ждать ваших показаний счетчиков до 28 числа.')
        except:
            print(id)


async def get_id_user(message: types.Message):
    await bot.send_message(message.chat.id, f'Привет {message.chat.id}')


def register_handler_registration(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(comand_send, commands=['send'])
    dp.register_message_handler(get_id_user, commands=['id'])

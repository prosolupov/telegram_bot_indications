from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

from bd.operations import *

from create_bot import dp, bot
from keyboards import kb_service, kb_select


class FSMAddNumberLs(StatesGroup):
    addNumber = State()
    ls = State()


async def start_add_ls(message: types.Message):

    kb_select = InlineKeyboardMarkup(resize_keyboard=False, one_time_keyboard=True)
    b_yes = InlineKeyboardButton(text="Да", callback_data='addLs_yes')
    b_no = InlineKeyboardButton(text="Нет", callback_data='addLs_no')
    kb_select.add(b_yes, b_no)

    number_ls = getNumberLs(message.from_user.id)
    await bot.send_message(message.chat.id, f'К вашему аккаунту привязан лицевой счет № {number_ls}.\n'
                                                f'Хотите привязать ёще один лицевой счёт?', reply_markup=kb_select)


@dp.callback_query_handler(Text(startswith='addLs_'), state=None)
async def answer_yes(callback: types.CallbackQuery):
    result = callback.data.split('_')[1]
    if result == 'yes':
        await callback.message.answer(f'Введите лицевой счет из 13 чисел.'
                                      f'\n Лицевой счёт должен начинатся с 554')
        await callback.answer()
        await FSMAddNumberLs.addNumber.set()
    elif result == 'no':
        await callback.answer()
        await callback.message.answer(f'Хорошо')
    #await message.reply("Введите лицевой счет из 13 чисел. Лицевой должен начинатся с 554")


async def add_new_ls(message: types.Message, state=FSMContext):
    result = addLsUser(int(message.text), message.from_user.id)
    await state.finish()


def register_handler_add_number(dp: Dispatcher):
    dp.register_message_handler(start_add_ls, commands=['registration'], state=None)
    dp.register_message_handler(add_new_ls, state=FSMAddNumberLs.addNumber)
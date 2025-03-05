from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from bd.operations import findIdLs
from aiogram.dispatcher.filters import Text
from create_bot import dp, bot
from bd.operations import *
from hadlers.counter.showCounter import change_country
from hadlers.start import command_start
from keyboards import kb_country


class FSMIndications(StatesGroup):
    indication = State()
    setIndication = State()


idCount = ''


@dp.callback_query_handler(Text(startswith='id_'), state=None)
async def id_call(callback: types.CallbackQuery):
    await FSMIndications.indication.set()
    global idCount
    idCount = callback.data.split('_')[1]
    await callback.message.answer('Введите новые показания счетчика')
    await callback.answer()


@dp.message_handler(state=FSMIndications.indication)
async def setIndication(message: types.Message, state=FSMContext):

    if int(getIndication(idCount)) <= int(message.text):
        setNewIndication(idCount, message.text)
        await message.reply("Новые показания успешно записаны")
        await state.finish()
        await change_country(message)
        #await bot.send_message(message.chat.id, f'Выберите пунк меню', reply_markup=kb_country)
    else:
        await message.reply("Новые показания должны быть больше, или равны текущим")

    async with state.proxy() as data:
        data['setIndication'] = message.text


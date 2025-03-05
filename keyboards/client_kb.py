from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton

b1 = KeyboardButton('/Регистрация')
kb_registration = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_registration.add(b1)

#Service
b_country = KeyboardButton('/Счетчики')
b_calculation = KeyboardButton('/Начисления')
b_owner = KeyboardButton('/Собственник')
kb_service = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_service.add(b_country).add(b_calculation).add(b_owner)

#Country
b_change_country = KeyboardButton('/Показания')
b_1_country = KeyboardButton('/Смена_счетчика')
#b_2_country = KeyboardButton('/Услуга 2')
#b_3_country = KeyboardButton('/Услуга 1')
kb_country = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_country.add(b_change_country).add(b_1_country)#.add(b_2_country).add(b_3_country)

#Начисления
b_calculation = KeyboardButton('/Задолженность')
#b_calculation1 = KeyboardButton('/Услуга1')
#b_calculation2 = KeyboardButton('/Услуга2')
kb_calculation = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_calculation.add(b_calculation)#.add(b_calculation1).add(b_calculation2)

#Собственник
b_owner1 = KeyboardButton('/Услуга1')
b_owner2 = KeyboardButton('/Услуга1')
b_owner3 = KeyboardButton('/Услуга1')
kb_owner = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_owner.add(b_owner1).add(b_owner2).add(b_owner3)

#Выбор
kb_select = InlineKeyboardMarkup(resize_keyboard=False, one_time_keyboard=True)
b_yes = InlineKeyboardButton(text="Да", callback_data='yes')
b_no = InlineKeyboardButton(text="Нет", callback_data='no')
kb_select.add(b_yes, b_no)
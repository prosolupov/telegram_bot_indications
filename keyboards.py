from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

inline_btn_1 = InlineKeyboardButton('Регистрация', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
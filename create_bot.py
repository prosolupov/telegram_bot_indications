from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand, BotCommandScopeDefault, message

#TOKEN = "5205949851:AAGZEvYAe-rdBIf90a7e-5qa633jMBCqXAE"
TOKEN = "6649097753:AAHJepy_GHIvvlx5qCYyE_wwHQ7NF39IWCQ"

storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


from aiogram.utils import executor
from create_bot import dp

from hadlers import registration
from hadlers import start
from hadlers import addNumbersLs
from hadlers.counter import showCounter, newSetupCounter
from hadlers.payment import showСalculation

registration.register_handler_registration(dp)
start.register_handler_registration(dp)
showCounter.show_counter_handler(dp)
newSetupCounter.new_setup_counter_handler(dp)
addNumbersLs.register_handler_add_number(dp)
showСalculation.show_calculation_handler(dp)


executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    executor.start_polling(dp)

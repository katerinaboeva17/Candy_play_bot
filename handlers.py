from aiogram import types, Dispatcher
import commands


def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start, commands=['start'])
    dp.register_message_handler(commands.level_1, commands=['level_1'])
    dp.register_message_handler(commands.level_2, commands=['level_2'])
    dp.register_message_handler(commands.set_total_candies, commands=['set'])
    dp.register_message_handler(commands.set_max_take, commands=['set_max'])

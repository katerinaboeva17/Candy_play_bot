from aiogram import types
from create_bot import bot
import model



async def hello(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}! Сегодня будем делить конфеты. '
                                      f'Но все конфеты достанутся игроку, который заберёт последнюю конфету. '
                                      f'Для управления игрой используй команды: '
                                      f'/start - начать игру; '
                                      f'/level_1 - выбрать лёгкий уровень; '
                                      f'/level_2 - выбрать сложный уровень; '
                                      f'/set - выбрать количество конфет на кону; '
                                      f'/set_max - выбрать максимальное количество конфет, которое можно взять за один ход. ')

async def winner(message: types.Message):
    await bot.send_message(message.from_user.id, f'Поздравляю с победой, {message.from_user.first_name}!')

async def take_null(message: types.Message):
    await bot.send_message(message.from_user.id, 'Возьми хоть сколько - нибудь...')

async def take_many(message: types.Message):
    await bot.send_message(message.from_user.id, 'А не многовато ли взяли?')

async def unknown(message: types.Message):
    await bot.send_message(message.from_user.id, 'А это что такое? Попробуй ещё раз! ')

async def play(message: types.Message):
    total_count = model.get_total_candies()
    player_take = int(message.text)
    total = total_count - player_take
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name} взял {player_take} конфет, и на столе осталось {total} конфет')


    


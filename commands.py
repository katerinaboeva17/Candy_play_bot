from aiogram import types
from create_bot import bot
import model
import random
import asyncio 
from create_bot import dp
import view

async def start(message: types.Message):
    player = message.from_user
    model.set_players_id(player)
    await view.hello(message)
    
    
async def level_1(message: types.Message):
    dp.register_message_handler(player_turn1)
    player = message.from_user
    model.set_players_id(player)
    first_turn = random.randint(0, 1)
    if first_turn:
        await await_player(player)
    else:
        await enemy_turn1(player)


async def level_2(message: types.Message):
    dp.register_message_handler(player_turn2)
    player = message.from_user
    model.set_players_id(player)
    first_turn = 0
    if first_turn:
        await await_player(player)
    else:
        await enemy_turn2(player)


async def player_turn1(message: types.Message):
    player = message.from_user
    model.set_players_id(player)
    max_take = model.get_max_take()
    if (message.text).isdigit():
        if 0 < int (message.text) < max_take + 1:
            total_count = model.get_total_candies()
            player_take = int(message.text)
            total = total_count - player_take
            await view.play(message)
            if model.check_win(total):
                await view.winner(message)
                return
            model.set_total_candies(total)
            await enemy_turn1(player)
        elif int (message.text) == 0:
            await view.take_null(message)
        else:
            await view.take_many(message)
    else:
         await view.unknown(message)



async def player_turn2(message: types.Message):
    player = message.from_user
    model.set_players_id(player)
    max_take = model.get_max_take()
    if (message.text).isdigit():
        if 0 < int (message.text) < max_take + 1:
            total_count = model.get_total_candies()
            player_take = int(message.text)
            total = total_count - player_take
            await view.play(message)
            if model.check_win(total):
                await view.winner(message)
                return
            model.set_total_candies(total)
            await enemy_turn2(player)
        elif int (message.text) == 0:
            await view.take_null(message)
        else:
            await view.take_many(message)
    else:
         await view.unknown(message)


async def enemy_turn2(player):
    total_count = model.get_total_candies()
    max_take = model.get_max_take()
    if total_count < max_take + 1:
        enemy_take = total_count
    else:
        enemy_take = (total_count-1) % max_take
    total = total_count - enemy_take
    if model.check_win(total):
        await bot.send_message(player.id, f'{player.first_name}, ты проиграл. Тебя сделала железяка!')

        return
    model.set_total_candies(total)
    await bot.send_message(player.id, f'Бот взял {enemy_take} конфет, и на столе осталось {total} конфет')
    await asyncio.sleep(5)
    await await_player(player)

async def enemy_turn1(player):
    total_count = model.get_total_candies()
    max_take = model.get_max_take()
    if total_count < max_take + 1:
        enemy_take = total_count
    else:
        enemy_take = random.randint(1, max_take)
    total = total_count - enemy_take
    if model.check_win(total):
        await bot.send_message(player.id, f'{player.first_name}, ты проиграл. Тебя сделала железяка!')
        return
    model.set_total_candies(total)
    await bot.send_message(player.id, f'Бот взял {enemy_take} конфет, и на столе осталось {total} конфет')
    await asyncio.sleep(5)
    await await_player(player)


async def await_player(player):
    max_take = model.get_max_take()
    await bot.send_message(player.id, f'{player.first_name}, бери конфеты, но не больше {max_take}.')


async def set_max_take(message: types.Message):
    num = int((message.text).split(' ')[1])
    model.set_max_take(num)
    await bot.send_message(message.from_user.id, f'Максимальное количество конфет, которое можно взять за один ход, изменили на {num}')
        

async def set_total_candies(message: types.Message):
    count = int((message.text).split(' ')[1])
    model.set_total_candies(count)
    await bot.send_message(message.from_user.id, f'Количество конфет на кону изменили на {count}')
        
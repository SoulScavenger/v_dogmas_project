import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
import aiohttp


from tokens import SITE_TOKEN, TELEGRAM_BOT_TOKEN

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()
header = {'Authorization': f'Token {SITE_TOKEN}'}


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!')


@dp.message(Command('commands'))
async def get_all_commands(message: Message):
    url = "http://127.0.0.1:8000/api/v1/commands/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=header) as response:
            commands = await response.json()
    try:
        for command in commands[::-1]:
            await message.answer(
                f"---------------ID команды: {command['id']}---------------\n"
                f"Название команды:\n{command['name']},\n"
                "-----------------------------------------------------------\n"
                f"Синтаксис команды:\n{command['syntax']},\n"
                "-----------------------------------------------------------\n"
                f"Подробное описание:\n{command['description']}"
            )
    except AttributeError:
        await message.answer(commands['detail'])


@dp.message(F.text.contains('/command'))
async def get_command(message: Message):

    if isinstance(message.text, str):
        command_id = message.text.split()[-1]

    url = f"http://127.0.0.1:8000/api/v1/commands/{command_id}/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=header) as response:
            command = await response.json()
    try:
        await message.answer(
            f"-----------------ID команды: {command['id']}-----------------\n"
            f"Название команды:\n{command['name']},\n"
            "---------------------------------------------------------------\n"
            f"Синтаксис команды:\n{command['syntax']},\n"
            "---------------------------------------------------------------\n"
            f"Подробное описание:\n{command['description']}"
        )
    except KeyError:
        await message.answer('Такой команды не существует...')
    except aiohttp.ContentTypeError:
        await message.answer('Такой команды не существует...')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')

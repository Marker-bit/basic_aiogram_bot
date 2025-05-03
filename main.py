import asyncio
import logging

import environs
from aiogram import Bot, Dispatcher, enums
from aiogram.client.default import DefaultBotProperties

from handlers import start

logging.basicConfig(level=logging.DEBUG)

env = environs.Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")


async def main():
    bot = Bot(
        BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=enums.ParseMode.HTML),
    )
    dp = Dispatcher()
    dp.include_routers(start.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

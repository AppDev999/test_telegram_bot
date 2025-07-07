import logging
import asyncio
import os

from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

# All handlers should be attached to the Router (or Dispatcher)
from aiogram.types import Message
from aiogram.filters import CommandStart

dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Hello! I'm a bot.")


@dp.message()
async def handle_messages(message: Message):
    await message.answer(text=message.text)


async def main() -> None:
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    bot = Bot(
        token=bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

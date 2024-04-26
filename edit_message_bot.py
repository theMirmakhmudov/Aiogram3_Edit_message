import asyncio
import time
from aiogram import Bot, Dispatcher, types, F
import logging
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import ReactionTypeEmoji

from config import TOKEN

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"<b>Assalomu Aleykum\nXurmatli {message.from_user.mention_html()}</b>")


@dp.message(Command("edit"))
async def cmd_help(message: types.Message, bot: Bot):
    edit = await message.answer("11")
    await bot.edit_message_text(chat_id=message.chat.id, message_id=edit.message_id, text="10")
    time.sleep(1)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=edit.message_id, text="9")
    time.sleep(1)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=edit.message_id, text="8")
    time.sleep(1)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=edit.message_id, text="7")
    time.sleep(1)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=edit.message_id, text="6")
    time.sleep(1)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=edit.message_id, text="5")
    time.sleep(1)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=edit.message_id, text="4")
    time.sleep(1)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=edit.message_id, text="3")
    time.sleep(1)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=edit.message_id, text="2")
    time.sleep(1)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=edit.message_id, text="1")
    time.sleep(1)
    await bot.delete_message(chat_id=message.chat.id, message_id=edit.message_id)


async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

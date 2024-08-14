from telethon import TelegramClient
from telebot import TeleBot
import time, re

from sub_function import check_text
from config import API_ID, API_HASH, TG_BOT_TOKEN

client = TelegramClient("../session_tg", API_ID, API_HASH)
bot = TeleBot(TG_BOT_TOKEN)

async def main():
    dialogs = await client.get_dialogs()
    
    
    for dialog in dialogs:
        if dialog.title == "Message":
            messages = client.iter_messages(dialog)
            last_message = await messages.__anext__()
            # сделать так чтоб создатель тоже мог отправлять сообщения
            a = await check_text(last_message.text)
            print(a)


with client:
    client.loop.run_until_complete(main())
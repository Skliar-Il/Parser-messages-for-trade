from typing import List
from telebot import TeleBot
from config import TG_BOT_TOKEN
import time, re, asyncio

from schemas import Schema_Check_Text

bot = TeleBot(TG_BOT_TOKEN)


async def check_text(text: str):
    
    if re.search(r'#admin', text):
        item = "message"
        cut = 7
        type = "admin_message"

        return Schema_Check_Text(securities=item, cut=cut, type=type, change=0)
    
    try:
        item = re.search(r' [A-Z]+:', text)
        cut = int(item.span()[0]+1)
        item = item[0][1:-1]

        if re.search(r'открытия', text):
            type = "change_open"
            change = float(re.search(r'\d+[.]?[\d]?', text)[0])

        elif re.search(r'Крупная', text):
            type = "many_lot"
            change = float(re.search(r'\d+[.]+\d+', text)[0])*1000000

        elif re.search(r'Резкое', text):
            type = "change_volume"
            change = float(re.search(r'\d+[.]+\d?', text)[0])

        
        return Schema_Check_Text(securities=item, cut=cut, type=type, change=change)
    
    except Exception as exception:
        return Schema_Check_Text(securities="None", cut=0, type="error", change=0, error=str(exception))

async def send_message_users(tg_id: List[int], text: str):
    for id in tg_id:
        bot.send_message(id, text)



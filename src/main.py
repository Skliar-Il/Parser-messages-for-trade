from telethon import TelegramClient
from telebot import TeleBot
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_, insert
from redis import Redis
import time, re

from sup_function import check_text, send_message_users
from database import async_session_factory, redis_connection_pool
from models.tables import *
from config import API_ID, API_HASH, TG_BOT_TOKEN, MAIN_ADMIN_TG_ID

client = TelegramClient("../session_tg", API_ID, API_HASH)
bot = TeleBot(TG_BOT_TOKEN)

async def main():
    dialogs = await client.get_dialogs()
    
    
    for dialog in dialogs:
        if dialog.title == "Message":
            redis = Redis(connection_pool=redis_connection_pool)
            
            while True:
                messages = client.iter_messages(dialog)
                last_message = await messages.__anext__()
                
                try:
                    cache_last_message = redis.get("last_message") 
                    str_last_message = str(last_message.text)
                    
                    if cache_last_message.decode() == str_last_message:
                        time.sleep(1)
                        continue
                    
                except:
                    redis.set("last_message", str_last_message)
                                        
                message_information = await check_text(last_message.text)

                if message_information.type == "change_open":
                    async with async_session_factory() as session: 
                        users_tg_id = await session.execute(select(Table_Subscribe.tg_id)
                                                          .where(or_(Table_Subscribe.type_change_open == 0, 
                                                                     Table_Subscribe.type_change_open <= message_information.change), 
                                                                 Table_Subscribe.days_subscribe > 0,
                                                                 getattr(Table_Subscribe, message_information.securities) == True))

                        users_tg_id = users_tg_id.scalars().all()
                        #print(message_information)
                        await send_message_users(users_tg_id, last_message.text[message_information.cut:])

                elif message_information.type == "many_lot":
                    async with async_session_factory() as session:
                        users_tg_id = await session.execute(select(Table_Subscribe)
                                                            .where(or_(Table_Subscribe.type_many_lot == 0,
                                                                       Table_Subscribe.type_many_lot <= message_information.change),
                                                                   Table_Subscribe.days_subscribe > 0,
                                                                   getattr(Table_Subscribe, message_information.securities) == True))

                        users_tg_id = users_tg_id.scalars().all()
                        #print(message_information)
                        await send_message_users(users_tg_id, last_message.text[message_information.cut:])

                elif message_information.type == "change_volume":
                    async with async_session_factory() as session:
                        users_tg_id = await session.execute(select(Table_Subscribe.tg_id)
                                                            .where(or_(Table_Subscribe.type_change_volume == 0,
                                                                       Table_Subscribe.type_change_volume <= message_information.change),
                                                                   Table_Subscribe.days_subscribe > 0,
                                                                   getattr(Table_Subscribe, message_information.securities) == True))

    
                        users_tg_id = users_tg_id.scalars().all()
                        #print(message_information)
                        await send_message_users(users_tg_id, last_message.text[message_information.cut:])

                elif message_information.type == "admin_message":
                    async with async_session_factory() as session:
                        users_tg_id = await session.execute(select(Table_Subscribe.tg_id))
                        users_tg_id = users_tg_id.scalars().all()
                        
                        await send_message_users(users_tg_id, f"❗❗❗Сообщение от администрации❗❗❗ \n\n{last_message.text[message_information.cut:]}")
                        #print(f"❗❗❗Сообщение от администрации❗❗❗ \n\n{last_message.text[message_information.cut:]}")
                
                
                elif message_information.type == "error":
                    bot.send_message(MAIN_ADMIN_TG_ID, text=f"❗❗❗ERROR❗❗❗ \n detail: \n\n{message_information.error}")
                
                redis.set("last_message", str_last_message)
                time.sleep(1)
                      
                     
                    

while True:
    try:
        with client:
            client.loop.run_until_complete(main())
            
    except:
        time.sleep(1)
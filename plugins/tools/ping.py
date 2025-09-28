from pyrogram import Client, filters
from plugins.utility.db import is_user_registered
import asyncio,time

@Client.on_message(filters.command("ping", prefixes=["/", "."]))
async def ping(bot, message):
    if not await is_user_registered(message.from_user.id):
        await message.reply_text("You are not registered. Use /register to register.",quote=True)
        return
    start_time = time.time()
    x = await message.reply_text("Pong...", quote=True)
    end_time = time.time()
    duration = end_time - start_time
    await x.edit(f"Ping: <code>{duration*1000:.2f}ms </code>")

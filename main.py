import asyncio
from pyrogram import Client, filters

Bot = Client(session_name="buddodiforwardtagremover",bot_token="Bot Token",api_hash="API HASH", api_id=API ID)
@Bot.on_message(filters.private or filters.forwarded)
async def remover(client,message):
	await message.copy(chat_id=message.from_user.id)
Bot.run()

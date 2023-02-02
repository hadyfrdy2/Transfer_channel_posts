from pyrogram import Client , filters , idle, __version__
from pyrogram.types import *
import time
from pyrogram.errors import FloodWait
from pyrogram.raw import *
from pyromod import listen

id = 12345678
hash = "Hash from telegram" 
app = Client("sender"  , api_id= id, api_hash=hash)


admin = 123456789
msg_id = []
help = f"""
`send id1 id2`
**در id1 ایدی عددی کانالی که میخوای پستاش فوروارد کنی**
**در id2 ایدی عددی کانالی که میخوای پست ها فوروارد شه**
`join link`
**جای link لینک یا ایدی کانال مورد نظر**
    """
@app.on_message(filters.private&filters.user(admin))
async def reatarts(c,m):
	text=m.text
	chat_id=m.chat.id
	if text == 'help':
		await m.reply(help)
	elif text.startswith('join '):
		try:
			link = text.replace('join ','')
			await app.join_chat(link)
			await m.reply('- **join** ✅')
		except:
			await m.reply('- **error** ❌')
		

@app.on_message(filters.command("send",None) & filters.user(admin),group=1)
async def sends(client,message):
	if len(message.command) == 3:
		channel1 = message.command[1]
		channel2 = message.command[2]
		try:
			async for message in app.iter_history(channel1,reverse=True):
				await app.copy_message(channel2,channel1,message.message_id)
		except FloodWait as e:
			time.sleep(e.x)

		
app.start(), print('started...'), idle(), app.stop()
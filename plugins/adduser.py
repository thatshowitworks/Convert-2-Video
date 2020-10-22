from pyrogram import Filters
from bot import app
from helper_funcs.sql.approve import add_user, remove_user

@app.on_message(filters.command("adduser"))
async def add(client, update):
	     if update.from_user['id'] not in AUTH_USERS:
		       return
	     msg = update.text
	     reply_message = update.reply_to_message
	     if reply_message:
	         add_user(reply_message.from_user["id"], "k")
	         await update.reply("User approved to use bot")
	     else:
	       try:
	         user_id = int(msg.split(" ", 1)[1], "k")
	         add_user(user_id)
	         await update.reply("User approved to use bot")
	       except:
	         await message.reply("Format: `/adduser user id`")
	         return

@app.on_message(filters.command("rmuser"))
async def remove(client, update):
	     if update.from_user['id'] not in AUTH_USERS:
		       return
	     msg = update.text
	     reply_message = update.reply_to_message
	     if reply_message:
	         remove_user(reply_message.from_user["id"])
	         await update.reply("User unapproved to use bot")
	     else:
	       try:
	         user_id = int(msg.split(" ", 1)[1])
	         add_user(user_id)
	         await update.reply("User unapproved to use bot")
	       except:
	         await message.reply("Format: `/rmuser user id`")
	         return
	     	     

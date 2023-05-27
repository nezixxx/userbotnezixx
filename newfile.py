
from pyrogram import Client, filters

from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions

import time

from time import sleep

import random


import requests
import openai
from pyrogram import enums

api_id = 11296923

api_hash = "8ac3fa9ce8721453e48f528039bb7781"
openai.api_key = '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'

app = Client("my_account", api_id=api_id, api_hash=api_hash)


@app.on_message(filters.command("spam", prefixes=".") & filters.me)
def type(_, msg):
	
	#che = msg.text.split(".spam ", maxsplit=2)[0]
	
	che = msg.text.split()[1]
	he = msg.text.split(".spam " + che, maxsplit=10)[1]
	msg.edit(f"Запрос отправлен, считаю до числа: {che}\nmessage: {he[1:]}")
	sleep(0.5)
	pers = 1
	while(pers != (int(che) + 1)):
			app.send_message(msg.chat.id, f"{he[1:]}\n")
			pers += 1
	app.send_message(msg.chat.id, f"Операция завершена, я дошел до числа: {pers -1 }")

@app.on_message(filters.command("очистка", prefixes="."))
def thanos(_, msg):
	for member in app.get_chat_members(msg.chat.id):
	   	member = member
	   	msg.delete()
	   	prem = member.user.is_deleted
	   	id = member.user.id
	   	if prem == True:
	   		   app.send_message(msg.chat.id, f"Удален {member.user.id}")
	   		   app.ban_chat_member(
	   		   chat_id=msg.chat.id,
	   		   user_id=id
	   		   )
	   	else:
	   		app.send_message(2003573597, f"{member.user.first_name} чист {member.user.id}")

@app.on_message(filters.command("check", prefixes="."))
def thanos(_, msg):
    

    for member in app.get_chat_members(msg.chat.id):
    	member = member
    	msg.delete()
    	app.send_message(msg.chat.id, f"{member.user.id} | @{member.user.username} | <a href='tg://user?id={member.user.id}'>{member.user.first_name}</a>", parse_mode=enums.ParseMode.HTML)
    	
@app.on_message(filters.command("gen", prefixes="."))
def png(_, msg):
	query = " ".join(msg.text.split()[1:])
	response = openai.Image.create(prompt=query, n=1, size="1024x1024")
	image_url = response['data'][0]['url']
	print(image_url)
	response = requests.get(image_url)
	image_bytes = response.content
	app.send_photo(msg.chat.id, image_bytes)

@app.on_message(filters.command("пинг", prefixes="."))
def ping_pong(client, msg):
    start_time = time.time()
    sent = msg.edit("Понг!")
    end_time = time.time()
    ping_time_ms = round((end_time - start_time) * 1000, 2)
    sent.edit(f"⏱️ Время отклика: {ping_time_ms}мс")
     

	

@app.on_message(filters.command("timer", prefixes=".") & filters.me)
def type(_, msg):
	
	che = msg.text.split(".timer ", maxsplit=1)[1]
	msg.edit(f"Запрос отправлен, считаю до {che} секунд.")
	sleep(1)
	pers = 1
	while(pers != (int(che) + 1)):
			sleep(1)
			sl = int(che) - int(pers)
			m = round(int(che) / 60)
			th = f"{m}м. {int(che) - (m * 60)} секунд"
			if int(sl) > 60:
				mn = int(sl) / 60
				msg.edit(f"Цель: {th}\nНасчитано: {pers} секунд\nОсталось: {round(mn)} минут")
				pers += 1
			else:
				msg.edit(f"Цель: {th}\nНасчитано: {pers} секунд\nОсталось: {sl} секунд")
				pers += 1
	msg.edit("Время вышло!")

@app.on_message(filters.command("go", prefixes=".") & filters.me)
def type(_, msg):
	
	che = msg.text.split(".go ", maxsplit=1)[1]
	msg.edit(f"Запрос отправлен, считаю до числа: {che}")
	sleep(0.5)
	pers = 1
	while(pers != (int(che) + 1)):
			app.send_message(msg.chat.id, f" {pers}\n")
			pers += 1
	app.send_message(msg.chat.id, f"Операция завершена, я дошел до числа: {pers -1 }")
# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)

def type(_, msg):
	
	orig_text = msg.text.split(".type ", maxsplit=1)[1]
	
	text = orig_text
	
	tbp = "" # to be printed
	
	typing_symbol = "▒"
	

	while(tbp != orig_text):
		
		try:
			
			msg.edit(tbp + typing_symbol)
			sleep(0.05) # 50 ms
			
			
			tbp = tbp + text[0]
			text = text[1:]
			
			
			msg.edit(tbp)
			sleep(0.05)
			

		except FloodWait as e:
			
			sleep(e.x)

app.run()
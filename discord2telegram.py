#!/usr/bin/env python
# -*- coding: utf-8 -*-

# INSTALL #
# sudo pip install telepot
# sudo pip install discord.py

import discord
import sys
import time
import pprint
import telepot
import json

user_id = ""
group = ''
chat_id = ''

discord_email = ""
discord_passwd = ""
discord_confirence_id = ""
telegram_token = ""

discord_client = discord.Client()
discord_client.login(discord_email, discord_passwd)

@discord_client.event
def on_message(message):
	log = message.content
	name = message.author.name
	discord_msg = (name+': '+log).encode('utf-8')
	print discord_msg
	# print log
	telegram_bot.sendMessage(chat_id, discord_msg)

@discord_client.event
def on_ready():
	print('Logged in as')
	print(discord_client.user.name)
	print(discord_client.user.id)

def dicord_send_to_channel(content):
    for server in discord_client.servers:
        for channel in server.channels:
                discord_client.send_message(channel, content)

def handle(msg):
	text = msg.get('text')
	# c_id = chat_id
	user_id = msg.get('chat').get('id')
	print user_id
	print text
	dicord_send_to_channel(text)

telegram_bot = telepot.Bot(telegram_token)
telegram_bot.notifyOnMessage(handle)
discord_client.run()

while 1:
    time.sleep(10)

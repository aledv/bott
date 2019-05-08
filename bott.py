import telepot
import config
import os

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    user_id = msg['from']['id']
    if user_id != config.user_id:
    	bot.sendMessage(chat_id, "NOT AUTHORIZED!!!")
		return

    first_name = msg["from"]["first_name"]
    last_name = msg["from"]["last_name"]
    name = first_name.lstrip() + ' ' + last_name.lstrip()

    if content_type == 'text':
	    txt = msg['text']

		if txt == '/list':
			bot.sendMessage(chat_id, '/list - list of all commands \n/command1 - Description')
		elif txt == '/command1':
			os.system(config.commandsPath+"command1.sh")
			bot.sendMessage(chat_id, 'command1 executed!')
		else:
	        bot.sendMessage(chat_id, "Hi %s type /list for the list of all commands."%name)

    if content_type == 'audio':
		autor = msg['audio']['performer']
		title = msg['audio']['title']
		file_id = msg['audio']['file_id']
		name = autor.lstrip() +' - '+ title.lstrip() + '.mp3'

		if name != None:
	  		bot.download_file(file_id,config.savePath+name)
	  		bot.sendMessage(chat_id, 'Hi %s, %s saved!'%(sender_name,name))
	  		return

bot = telepot.Bot(config.token)
bot.message_loop(on_chat_message)

print 'Listening ...'

import time
while 1:
    time.sleep(10)

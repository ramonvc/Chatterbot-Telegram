from random import randrange
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
import asyncio
from telethon import TelegramClient, events
from telethon.tl.types import PeerUser, PeerChat, PeerChannel

chatbot = ChatBot("Robertin")  # Change bot name

convo = open('chat.txt', 'r').readline()  # Read a text file to train your first sentences

trainer = ListTrainer(chatbot)

trainer.train(convo)

api_id = ''  # Get API ID in Telethon TelegramCliente 
api_hash = ''  # Get API HASH in Telethon TelegramCliente 
def main():
    client = TelegramClient('telehandler_session', api_id, api_hash)
    client.start()

    @client.on(events.NewMessage(incoming=True))
    async def handler(event):
        blacklist = open('blacklist.txt', 'r')  # Reads a "Blacklist.txt" text file. to avoid learning phrases with offensive words

        ignorar = False
        request = str(event.raw_text)
        print(request)
        for linha in blacklist:
            if linha[0:len(linha)-1] in request.lower().replace(" ", ""):
                ignorar = True
        if ignorar:
            response = "Isso não é legal, amg"
        else:
            response = str(chatbot.get_response(request))
        await event.reply(response)

    client.run_until_disconnected()


if __name__ == '__main__':
    main()

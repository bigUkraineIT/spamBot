import time
from telethon.sync import TelegramClient, events
print("Api_id: ")
api_id = input()
print("Hash_id: ")
api_hash = input()
print("Username to spam: ")
username = input()
print("Text to spam: ")
spamText = input()

with TelegramClient('name', api_id, api_hash) as client:
   while (1!=0):
      for i in range(12):
         client.send_message(username, spamText)
      print("12 messages have been sended! Sleep for 6 sec")
      time.sleep(6)

   client.run_until_disconnected()
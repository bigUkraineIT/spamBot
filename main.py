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
print("msgs in sec: ")
msgSec = int(input())
print("timeSleep: ")
timeSleep = int(input())

with TelegramClient('name', api_id, api_hash) as client:
   while (1!=0):
      for i in range(msgSec):
         client.send_message(username, spamText)
      time.sleep(timeSleep)

   client.run_until_disconnected()
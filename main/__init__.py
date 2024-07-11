#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = config("29868868", default=None, cast=int)
API_HASH = config("6b7bd10846ff6d7e8f50a4bfe13c9fd4", default=None)
BOT_TOKEN = config("7104952127:AAE4PfHU0zfW1UzHC7R3piCUjgg7JOLZh8w", default=None)
SESSION = config("BQHHw0QATpKlCWIBl65IFB6tuMnAiwF2N3mC3zFUFYM5FHYBO9blNfkpMqjDKBOlrG8cSyo6Hst4BWu1k0DZEEFUOPqP3Rd6OtOr8uceRwI21oB03buHZC_lXFM7nvKIuqmZ2_Do8mv-4kPkg1WcL3ij8N7VxU-qXtpc9W3VtQOc686o-xLlOlcCqu8Yw6NdAeI7uxvlmo4tGPJZsd50ZOQkq0zJbXMOUn2OHMH-ceFOiORjaGQ-2H7uh8xXrwm_vep4ty3dacQJ2bWEP5YYmKFPBOltt592Z1efpAVCPtfwPs0ZIDx9BrvGCVghNZO0bWrSP8miWgw9MUMWQxn3znW2JGFqGwAAAAFexUORAA", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("PPCNETWORKZ", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)

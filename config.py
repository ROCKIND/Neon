
import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

DS_API_ID = int(environ.get("DS_API_ID", "16536417"))
DS_API_HASH = environ.get("DS_API_HASH", "f6e58a549da642d7b765744a2f82c6d9")
DS_BOT_TOKEN = environ.get("DS_BOT_TOKEN", "7878910120:AAH7LbPPwmru54IAMGxA0l9KrLSGfugJ08k")
DS_BOT_USERNAME = environ.get("DS_BOT_USERNAME", "Silent_Adult_Bot") # bot username without @
DS_LOG_CHANNEL = int(environ.get("DS_LOG_CHANNEL", "-1002609521633"))
DS_STICKER = environ.get("DS_STICKER", "CAACAgIAAxkBAAKxemhQQxjjYapRz_MnIaOVoeX2QwaZAAL_TAACmcgQSd6zWuf0AdV3NgQ")
DS_PIC = environ.get('DS_PIC', 'https://envs.sh/pi.jpg/HGBOTZ.jpg')

# Database Channel For Text Or Caption Store 
DS_DESI_FILE_CHANNEL = int(environ.get("DS_DESI_FILE_CHANNEL", "-1002817464273"))
DS_VIDESI_FILE_CHANNEL = int(environ.get("DS_VIDESI_FILE_CHANNEL", "-1002887416583"))
FREE_LIMIT_DESI = 10
FREE_LIMIT_VIDESI = 3
PREMIUM_LIMIT_DESI = 40
PREMIUM_LIMIT_VIDESI = 15

# Bot Admins
try:
    DS_ADMINS=[]
    for x in (environ.get("DS_ADMINS", "1562935405 7989859892").split()):
        DS_ADMINS.append(int(x))
except ValueError:
      raise Exception("Your Admins list does not contain valid integers.")
    
# Mongodb Database 
DS_DB_URI = environ.get("DS_DB_URI", "mongodb+srv://Botmaster:Botmaster@cluster08283746473883.mfjsvds.mongodb.net/?retryWrites=true&w=majority&appName=Cluster08283746473883")
DS_DB_NAME = environ.get("DS_DB_NAME", "silentghost")

# True Or False
DS_FORWARD = bool(environ.get("DS_FORWARD", False))

# Force subscribe channel 
DS_AUTH_CHANNEL = int(environ.get('DS_AUTH_CHANNEL', '-1002609521633')) # give your force subscribe channel id here else leave it blank

# Verification Variables
DS_API = environ.get("DS_API", "a5515d390b300450bc0f19bd205f552be8082b40") # shortlink api
DS_URL = environ.get("DS_URL", "linkcents.com") # shortlink domain without https://
DS_VERIFY_TUTORIAL = environ.get("DS_VERIFY_TUTORIAL", "https://t.me/Robo_5_0/44") # how to open link 
DS_VERIFICATION = bool(environ.get("DS_VERIFICATION", True)) # set True Or False and make sure spelling is correct and first letter capital.

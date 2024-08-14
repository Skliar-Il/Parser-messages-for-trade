from dotenv import load_dotenv
import sys, os 

load_dotenv()

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")

POSTGRES_PASSWORD=os.environ.get("POSTGRES_PASSWORD")
POSTGRES_NAME=os.environ.get("POSTGRES_NAME")
POSTGRES_USER=os.environ.get("POSTGRES_USER")
POSTGRES_PORT=os.environ.get("POSTGRES_PORT")
POSTGRES_HOST=os.environ.get("POSTGRES_HOST")

REDIS_PORT=os.environ.get("REDIS_PORT")
REDIS_HOST=os.environ.get("REDIS_HOST")






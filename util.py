import os
import requests
from dotenv import load_dotenv
from typing import Final

load_dotenv()
TOKEN: Final = os.getenv("TOKEN")
CHAT_ID: Final = os.getenv("CHAT_ID")


def chatbot(message: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    requests.get(url)

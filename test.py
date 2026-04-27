import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY    = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
ENDPOINT   = os.getenv("ALPACA_ENDPOINT", "https://api.alpaca.markets/v2")

headers = {
    "APCA-API-KEY-ID":     API_KEY,
    "APCA-API-SECRET-KEY": SECRET_KEY,
}

resp = requests.get(f"{ENDPOINT}/account", headers=headers)
print(f"Status: {resp.status_code}")
print(resp.json())

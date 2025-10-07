import requests
import json
from parse_template import *

def send_message_to_discord(discord_json, message):
    """
    discord_json: str
        Path to the JSON file containing the Discord webhook URL
    message: str
        Message to send
    """
    with open(discord_json, "r") as f:
        data = json.load(f)
    mUrl = data.get("webhook_url")
    if not mUrl:
        print("Webhook URL not found in JSON file.")
        return
    data = {"content": message}
    response = requests.post(mUrl, json=data)
    print(response.status_code)
    print(response.content)


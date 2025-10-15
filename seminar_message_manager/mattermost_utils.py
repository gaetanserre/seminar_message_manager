import requests
import json


def send_message_to_mattermost(mattermost_json, message):
    """
    mattermost_json: str
        Path to the JSON file containing the Mattermost webhook URL
    message: str
        Message to send
    """
    with open(mattermost_json, "r") as f:
        data = json.load(f)
    mUrl = data.get("webhook_url")
    if not mUrl:
        print("Webhook URL not found in JSON file.")
        return
    data = {"text": message}
    response = requests.post(mUrl, json=data)
    print(response.status_code)
    print(response.content)

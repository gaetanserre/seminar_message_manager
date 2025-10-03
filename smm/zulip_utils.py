import zulip
import json


def move_old_messages_zulip(zulip_json):
    with open(zulip_json, "r") as f:
        zulip_data = json.load(f)

    client = zulip.Client(config_file=zulip_data["config_file"])
    bot_email = zulip_data["bot_email"]
    channel = zulip_data["channel"]
    topic = zulip_data["topic"]
    old_topic = zulip_data["old_topic"]

    request = {
        "anchor": "newest",
        "num_before": 100,
        "num_after": 0,
        "narrow": [
            {"operator": "sender", "operand": bot_email},
            {"operator": "channel", "operand": channel},
            {"operator": "topic", "operand": topic},
        ],
    }
    result = client.get_messages(request)
    message_ids = [msg["id"] for msg in result["messages"]]
    print(f"Found {len(message_ids)} messages to move.")
    for message_id in message_ids:
        request = {
            "message_id": message_id,
            "topic": old_topic,
        }
        client.update_message(request)
    print("Done.")


def send_message_to_zulip(zulip_json, msg):
    with open(zulip_json, "r") as f:
        zulip_data = json.load(f)

    client = zulip.Client(config_file=zulip_data["config_file"])
    channel = zulip_data["channel"]
    topic = zulip_data["topic"]

    request = {
        "type": "stream",
        "to": channel,
        "topic": topic,
        "content": msg,
    }
    client.send_message(request)

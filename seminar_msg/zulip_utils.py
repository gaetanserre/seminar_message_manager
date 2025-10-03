import zulip

channel = "seminars"
topic = "Seminar Infos"
old_topic = "OLD - Seminar Infos"
client = zulip.Client(config_file="./zuliprc")


def move_old_messages_zulip():
    """Move old messages from the bot in the `Seminar Infos` channel to `OLD - Seminar Infos`."""

    request = {
        "anchor": "newest",
        "num_before": 100,
        "num_after": 0,
        "narrow": [
            {"operator": "sender", "operand": "lips-seminars-bot@lips.zulipchat.com"},
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
        res = client.update_message(request)
    print("Done.")


def send_message_to_zulip(msg):
    request = {
        "type": "stream",
        "to": channel,
        "topic": topic,
        "content": msg,
    }
    result = client.send_message(request)

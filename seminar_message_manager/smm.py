import argparse
from .parse_template import parse_annoucement
from .zulip_utils import move_old_messages_zulip, send_message_to_zulip
from .mail_utils import send_email
from .discord_utils import send_message_to_discord


def cli():
    parser = argparse.ArgumentParser(
        description="Generate and send mails and Zulip announcement for seminar"
    )
    parser.add_argument("date", type=str, help="Date of the seminar (YYYY-MM-DD)")

    parser.add_argument(
        "--seminar_csv",
        type=str,
        default="seminars.csv",
        help="CSV file containing the seminar data",
    )
    parser.add_argument(
        "--zulip_json", type=str, default="zulip.json", help="Zulip json file"
    )
    parser.add_argument(
        "--mail_json", type=str, default="mail.json", help="Mail json file"
    )
    parser.add_argument(
        "--template_mail",
        type=str,
        default="templates/mail/announcement.html",
        help="Template mail to use",
    )
    parser.add_argument(
        "--template_zulip",
        type=str,
        default="templates/zulip/announcement.md",
        help="Template Zulip message to use",
    )
    parser.add_argument(
        "-s",
        "--send",
        action="store_true",
        help="Send the message to the Zulip topic and the mail to the mailing list",
    )
    parser.add_argument(
        "-sm", "--send_mail", action="store_true", help="Send the mail to the mailing list"
    )
    parser.add_argument(
        "-sz",
        "--send_zulip",
        action="store_true",
        help="Send the message to the Zulip topic",
    )
    parser.add_argument(
        "-sd",
        "--send_discord",
        action="store_true",
        help="Send the message to the Discord channel",
    )


    args = parser.parse_args()
    return args


def main():
    args = cli()
    mail = parse_annoucement(args.date, args.seminar_csv, args.template_mail)
    print(mail)
    zulip_msg = parse_annoucement(args.date, args.seminar_csv, args.template_zulip)
    print(zulip_msg)
    discord_msg = parse_annoucement(args.date, args.seminar_csv, args.template_discord)
    print(discord_msg)
    if args.send:
        args.send_mail = True
        args.send_zulip = True
        args.send_discord = True
    if args.send_mail:
        send_email(args.mail_json, mail)
        print("\n\033[1;32mMail sent\033[0m\n")
    if args.send_zulip:
        move_old_messages_zulip(args.zulip_json)
        send_message_to_zulip(args.zulip_json, zulip_msg)
        print("\n\033[1;32mZulip message sent\033[0m\n")
    if args.send_discord:
        send_message_to_discord(args.discord_json, discord_msg)
        print("\n\033[1;32mDiscord message sent\033[0m\n")

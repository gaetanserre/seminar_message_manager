import argparse
from .parse_template import parse_annoucement
from .zulip_utils import move_old_messages_zulip, send_message_to_zulip
from .mail_utils import send_email
from .discord_utils import send_message_to_discord
from .mattermost_utils import send_message_to_mattermost


def cli():
    parser = argparse.ArgumentParser(
        description="Generate and send mails, Zulip, Discord and Mattermost announcements for seminar"
    )
    parser.add_argument("date", type=str, help="Date of the seminar (YYYY-MM-DD)")

    parser.add_argument(
        "--seminar_csv",
        type=str,
        default="seminars.csv",
        help="CSV file containing the seminar data",
    )
    parser.add_argument(
        "--mail_json", type=str, default="mail.json", help="Mail json file"
    )
    parser.add_argument(
        "--zulip_json", type=str, default="zulip.json", help="Zulip json file"
    )
    parser.add_argument(
        "--discord_json", type=str, default="discord.json", help="Discord json file"
    )
    parser.add_argument(
        "--mattermost_json",
        type=str,
        default="mattermost.json",
        help="Mattermost json file",
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
        "--template_discord",
        type=str,
        default="templates/discord/announcement.md",
        help="Template Discord message to use",
    )
    parser.add_argument(
        "--template_mattermost",
        type=str,
        default="templates/mattermost/announcement.md",
        help="Template Mattermost message to use",
    )
    parser.add_argument(
        "-s",
        "--send",
        action="store_true",
        help="Send the message to the Zulip topic and the mail to the mailing list",
    )
    parser.add_argument(
        "-sm",
        "--send_mail",
        action="store_true",
        help="Send the mail to the mailing list",
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
    parser.add_argument(
        "-smt",
        "--send_mattermost",
        action="store_true",
        help="Send the message to the Mattermost channel",
    )

    args = parser.parse_args()
    return args


def main():
    args = cli()
    if args.send:
        args.send_mail = True
        args.send_zulip = True
        args.send_discord = True

    if args.template_mail and args.send_mail:
        mail = parse_annoucement(args.date, args.seminar_csv, args.template_mail)
        print(mail)
    if args.template_zulip and args.send_zulip:
        zulip_msg = parse_annoucement(args.date, args.seminar_csv, args.template_zulip)
        print(zulip_msg)
    if args.template_discord and args.send_discord:
        discord_msg = parse_annoucement(
            args.date, args.seminar_csv, args.template_discord
        )
        print(discord_msg)
    if args.template_mattermost and args.send_mattermost:
        mattermost_msg = parse_annoucement(
            args.date, args.seminar_csv, args.template_mattermost
        )
        print(mattermost_msg)

    if args.send_mail and args.template_mail and args.mail_json:
        send_email(args.mail_json, mail)
        print("\n\033[1;32mMail sent\033[0m\n")
    if args.send_zulip and args.template_zulip and args.zulip_json:
        move_old_messages_zulip(args.zulip_json)
        send_message_to_zulip(args.zulip_json, zulip_msg)
        print("\n\033[1;32mZulip message sent\033[0m\n")
    if args.send_discord and args.template_discord and args.discord_json:
        send_message_to_discord(args.discord_json, discord_msg)
        print("\n\033[1;32mDiscord message sent\033[0m\n")
    if args.send_mattermost and args.template_mattermost and args.mattermost_json:
        send_message_to_mattermost(args.mattermost_json, mattermost_msg)
        print("\n\033[1;32mMattermost message sent\033[0m\n")

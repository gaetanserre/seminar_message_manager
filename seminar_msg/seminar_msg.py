import argparse
from .parse_template import parse_annoucement
from .zulip_utils import move_old_messages_zulip, send_message_to_zulip
from .mail_utils import send_email


def cli():
    parser = argparse.ArgumentParser(
        description="Generate mails for the LIPS seminar series"
    )
    parser.add_argument("date", type=str, help="Date of the seminar (YYYY-MM-DD)")

    parser.add_argument(
        "--seminar_csv",
        type=str,
        default="seminars.csv",
        help="CSV file containing the seminar data",
    )
    parser.add_argument(
        "--zulip_secret", type=str, default="zuliprc", help="Zulip bot secret"
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
        help="Template zulip message to use",
    )
    parser.add_argument(
        "-s",
        "--send",
        action="store_true",
        help="Send the message to the Zulip channel (only for announcements)",
    )

    args = parser.parse_args()
    return args


def main():
    args = cli()
    mail = parse_annoucement(args.date, args.seminar_csv, args.template_mail)
    print(mail)
    print("\n\033[1;32mMail copied to clipboard\033[0m\n")
    zulip_msg = parse_annoucement(args.date, args.seminar_csv, args.template_zulip)
    print(zulip_msg)
    if args.send:
        send_email(args.mail_json, "LIPS Seminar Announcement", mail)
        print("\n\033[1;32mMail sent\033[0m\n")

        move_old_messages_zulip()
        send_message_to_zulip(zulip_msg)
        print("\n\033[1;32mZulip message sent\033[0m\n")

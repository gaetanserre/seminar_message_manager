import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json


def send_email(mail_json, content):
    with open(mail_json, "r") as f:
        mail_data = json.load(f)

    msg = MIMEMultipart()
    msg["From"] = mail_data["user"]
    msg["To"] = ", ".join(mail_data["to"])
    msg["Subject"] = mail_data["subject"]
    body = content
    msg.attach(MIMEText(body, "html"))

    with smtplib.SMTP(mail_data["smtp_server_domain_name"], 587) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(mail_data["user"], mail_data["password"])
        server.send_message(msg)

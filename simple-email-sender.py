from email.message import EmailMessage

import os
import ssl
import smtplib
import argparse

EMAIL_SENDER = os.environ.get("ES_EMAIL_SENDER")
EMAIL_APP_PASSWORD = os.environ.get("ES_EMAIL_APP_PASSWORD")


def main(receiver: str, subject: str, body: str):
    em = EmailMessage()
    em["From"] = EMAIL_SENDER
    em["To"] = receiver
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_APP_PASSWORD)
        smtp.send_message(em)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sends simple email messages.")
    parser.add_argument(
        "-r", help="The address the email message should be sent to", type=str
    )
    parser.add_argument("-s", help="The subject line of the email message", type=str)
    parser.add_argument(
        "-b", help="The three body content of the email message", type=str
    )
    args = parser.parse_args()
    main(args.r, args.s, args.b)

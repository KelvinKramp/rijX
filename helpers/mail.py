
from datetime import datetime as dt
import datetime
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
from helpers.confirmationmail import confirmationpart1, confirmationpart2
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()
# # SET VARIABLES FOR MAIL
# secrets = './secrets.json'
# with open(secrets) as f:
#     secret = json.load(f)
# developer = secret["developer"]
sender = os.environ.get("SENDER")
smtp_login = os.environ.get("SMTP_LOGIN")
password = os.environ.get("PASSWORD")
smtp_server = "smtp.mailgun.org"
port = "587"
date = ((str(dt.now(datetime.timezone.utc).day)+"-"+str(dt.now(datetime.timezone.utc).month)+"-"+str(dt.now(datetime.timezone.utc).year)))
subject = "Bevestigingsmail van RijbewijskeuringenRotterdam"


def send_message_mailgun(recipient, payment_link):
    html = confirmationpart1 +payment_link + confirmationpart2
    plain = "Dit is de betaallink: "+payment_link +". Klik op de link of kopieer en plak de link om te betalen."
    part1 = MIMEText(html, 'html')
    part2 = MIMEText(plain, 'plain')
    msg = MIMEMultipart('alternative')
    msg.attach(part2)
    msg.attach(part1)
    msg['Subject'] = subject
    msg['To'] = recipient
    msg['From'] = sender
    s = smtplib.SMTP(smtp_server, port)
    s.login(smtp_login, password)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()


if __name__ == '__main__':
    send_message_mailgun("k.h.kramp@gmail.com", "https://tikkie.me/pay/RijRdam/ucsqSFszXivucPSqxJgXKE")

from datetime import datetime as dt
import datetime
import smtplib
from email.mime.text import MIMEText
import os
from helpers.confirmationmail import confirmation_template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from dotenv import load_dotenv
load_dotenv()

sender = os.environ.get("SENDER")
smtp_login = os.environ.get("SMTP_LOGIN")
password = os.environ.get("PASSWORD")
smtp_server = "smtp.mailgun.org"
port = "587"
date = ((str(dt.now(datetime.timezone.utc).day)+"-"+str(dt.now(datetime.timezone.utc).month)+"-"+str(dt.now(datetime.timezone.utc).year)))
subject = "Bevestigingsmail van RijRotterdam"


def send_message_mailgun(recipient, datetime,address, type_service, worker, BIG, payment_link):
    html = Template(confirmation_template).safe_substitute(date_123=datetime,address_123=address, type_service=type_service, worker=worker, BIG=BIG, payment_link=payment_link)
    plain = "Uw afpsraak is gemaakt voor {datetime} op {address} voor type keuring {type_service}. U wordt geholpen door {worker} met BIG {BIG}. " \
            "Dit is de betaallink: {payment_link}. Klik op de link om te betalen en de afspraak te bevestigen.".format(datetime=datetime,address=address, type_service=type_service, worker=worker, BIG=BIG, payment_link=payment_link)
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

import os
import smtplib
from email.message import EmailMessage
from datetime import datetime as dt
import datetime
import smtplib
from email.mime.text import MIMEText
import os
from helpers.confirmationmail import confirmation_template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from string import Template
from definitions import ROOT_DIR
from dotenv import load_dotenv
load_dotenv()


def get_credentials():
    EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
    EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")
    SMTP_SERVER = os.environ.get("SMTP_SERVER")
    return EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_SERVER


def send_mail(recipient, subject=None, datetime_appointment=None, address=None, type_service=None, worker=None,
              BIG=None, payment_link=None, attachment=None, failed=False, message=None):

    # load credentials
    EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_SERVER = get_credentials()

    # if subject in message, send normal mail
    if subject:
        plain = message
        subject = subject
        part = MIMEText(plain, 'plain')
        msg = MIMEMultipart('alternative')
        msg.attach(part)

    # if backup failed sending send error message
    elif failed:
        plain = message
        subject = "BACKUP FAILED"
        part = MIMEText(plain, 'plain')
        msg = MIMEMultipart('alternative')
        msg.attach(part)

    # if attachment (backup file)
    elif attachment:
        msg = MIMEMultipart()
        body = "Backup"
        msg.attach(MIMEText(body, 'plain'))
        attachment = ROOT_DIR+str(attachment)
        attachment = open(attachment, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        date = ((str(dt.now(datetime.timezone.utc).day) + "-" + str(dt.now(datetime.timezone.utc).month) + "-" + str(
            dt.now(datetime.timezone.utc).year)))
        subject = "Encrypted backup file "+date+"-"+str(dt.now().time())[0:5]
        file_name = "backup-"+date+"-"+str(dt.now().time())[0:5].replace(":", "-")
        part.add_header('Content-Disposition', "attachment; filename= %s" % file_name)
        msg.attach(part)

    # otherwise send html plain mail, as an alternative send plain mail
    else:
        html = Template(confirmation_template).safe_substitute(date_123=datetime_appointment, address_123=address,
                                                               type_service=type_service, worker=worker, BIG=BIG,
                                                               payment_link=payment_link)
        plain = "Uw afpsraak is gemaakt voor {datetime} op {address} voor type keuring {type_service}. U wordt geholpen door {worker} met BIG {BIG}. " \
                "Dit is de betaallink: {payment_link}. Klik op de link om te betalen en de afspraak te bevestigen.".format(
            datetime=datetime_appointment, address=address, type_service=type_service, worker=worker, BIG=BIG,
            payment_link=payment_link)
        subject = "Bevestigingsmail van RijRotterdam"
        part1 = MIMEText(html, 'html')
        part2 = MIMEText(plain, 'plain')
        msg = MIMEMultipart('alternative')
        msg.attach(part2)
        msg.attach(part1)

    # set message configuration
    msg['From'] = os.environ.get("SENDER")
    msg['Subject'] = subject
    msg['To'] = recipient

    # send message
    with smtplib.SMTP_SSL(SMTP_SERVER, 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

if __name__ == "__main__":
    # TEST FAILED SENDING BACKUP
    # send_mail( "test@gmail.com", failed=True, message="test error message")

    # TEST SENDING BACKUP
    # send_mail("test@gmail.com", attachment="backup.csv" )

    # TEST SENDING MAIL WITH APPOINTMENT DETAILS
    # send_mail("test@gmail.com",)
    # data = {'BIG': 12311224,
    #         'address': 'Test address',
    #         'date': '14-04-2022 12:00',
    #         'email': 'k.h.kramp@gmail.com',
    #         'payment_link': 'https://tikkie,me/.../../../',
    #         'type_service': 'Medical Check €35,00',
    #         'worker': 'Dr. Test 5'}
    # send_mail(data["email"], datetime_appointment=data["date"], address=data["address"], type_service=data["type_service"], worker=data["worker"],
    #                      BIG=data["BIG"], payment_link=data["payment_link"])
    pass

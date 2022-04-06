import subprocess
from helpers.mail import send_mail
import os
from datetime import datetime as dt
import datetime
from dotenv import load_dotenv
load_dotenv()

# RUN TESTING UNIT
subprocess.run("python unittests.py 2> log.txt", shell=True)

# DEFINE SUBJECT TEXT FOR MAIL
attachment_file = "./log.txt"
with open(attachment_file, 'r') as f:
    log_file_text = f.read()
if not "ERROR" in str(log_file_text).upper():
    status = "OK"
else:
    status = "ERROR"
date = ((str(dt.now(datetime.timezone.utc).day)+"-"+str(dt.now(datetime.timezone.utc).month)+"-"+str(dt.now(datetime.timezone.utc).year)))
text = log_file_text
subject = "Unittest result " + date + ":" + status

# SEND MAIL
if status=="ERROR":
    send_mail(os.environ.get("DEVELOPER"), subject=subject, message=text)

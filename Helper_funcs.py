import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from bs4 import BeautifulSoup as bs
from  secrets_1 import Secrets

#class Email:

def send_email(to, subject, txt_to_send):
    From = "shsseniorassasin2024@hotmail.com"
    password = Secrets.Email_Password
    


    msg = MIMEMultipart()
    msg["From"] = From
    msg["To"] = ", ".join(to)
    msg["Subject"] = subject

    formatted_msg = MIMEText(txt_to_send, "plain")

    msg.attach(formatted_msg)



    server = smtplib.SMTP(host="smtp.office365.com", port=587)
    # connect to the SMTP server as TLS mode (secure) and send EHLO
    server.starttls()
    # login to the account using the credentials
    server.login(From, password)
    # send the email
    server.sendmail(From, to, msg.as_string())
    # terminate the SMTP session
    server.quit()






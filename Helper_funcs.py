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
    
    # to block email sending for testing comment out below statement

    password = Secrets.Email_Password
    
    # to block email sending for testing uncomment out below statements
    print ("email blocked for testing")
    password = ""
    #  

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





def Add_Target_Eliminated(person_name, email, Target_tracker_sheet_obj):
    row = Target_tracker_sheet_obj.find(person_name).row # find row of person
    Elim_target_name = Target_tracker_sheet_obj.acell(row, 3) # find old target name
    target_row = Target_tracker_sheet_obj.find(Elim_target_name).row # find old target row
    eliminated_target_email = Target_tracker_sheet_obj.acell(target_row, 2) # find eliminated persons email
    Targets_eliminated = Target_tracker_sheet_obj.acell(row, 5) # get all current targets eliminated
    new_Targets_eliminated = Targets_eliminated + ", " + Elim_target_name # add new eliminated target
    Target_tracker_sheet_obj.update_cell(row, 5, new_Targets_eliminated) # update sheet with new eliminated target
    new_target_name = Target_tracker_sheet_obj.acell(target_row, 3) # find new target name
    new_target_email = Target_tracker_sheet_obj.acell(target_row, 4) # find new target email
    Target_tracker_sheet_obj.update_cell(row, 3, new_target_name) #update new target name
    Target_tracker_sheet_obj.update_cell(row, 3, new_target_email) #update new target email

    print (email + ": " + f"Congratulations on your elimination, your new target is {new_target_name}")
    print (eliminated_target_email + ": " + f"Unfortunatly you have been eliminated by {person_name}")
    #send_email(email, "Senior Assass*n 2024: Elimination Confirmed", f"Congratulations on your elimination, your new target is {new_target_name}")
    #send_email(eliminated_target_email, "Senior Assass*n 2024: You Have Been Eliminated", f"Unfortunatly you have been eliminated by {person_name}")



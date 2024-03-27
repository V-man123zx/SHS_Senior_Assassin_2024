import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from bs4 import BeautifulSoup as bs
from  secrets_1 import Secrets
from time import sleep

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





def Add_Target_Eliminated(email, Target_tracker_sheet_obj, info_list_sheet_obj):
    Tracker_person_row = Target_tracker_sheet_obj.find(email).row # find row of person
    Person_Info_list_row = info_list_sheet_obj.find(email).row
    person_name = info_list_sheet_obj.cell(Person_Info_list_row, 2).value + " " + info_list_sheet_obj.cell(Person_Info_list_row, 3).value
    print ("person name: " + person_name)
    eliminated_target_email = Target_tracker_sheet_obj.cell(Tracker_person_row, 4).value # find old target email
    print ("Old target email: " + eliminated_target_email)
    Target_info_list_row = info_list_sheet_obj.find(eliminated_target_email).row
    Elim_target_name = info_list_sheet_obj.cell(Target_info_list_row, 2).value + " " + info_list_sheet_obj.cell(Target_info_list_row, 3).value
    print ("Eliminated Target Name: " + Elim_target_name)
    Tracker_target_row = Target_tracker_sheet_obj.find(eliminated_target_email, in_column=2).row # find old target row
    print ("Eliminated_Target_row: " + str(Tracker_target_row))

    Targets_eliminated = Target_tracker_sheet_obj.cell(Tracker_person_row, 5).value # get all current targets eliminated
    print ("Current targets Eliminated: " + str(Targets_eliminated))
    sleep(0.5)
    try:
        new_Targets_eliminated = Targets_eliminated + ", " + Elim_target_name # add new eliminated target
    except TypeError:
        new_Targets_eliminated = Elim_target_name
    print ("New Targets Eliminated: " + new_Targets_eliminated)
    Target_tracker_sheet_obj.update_cell(Tracker_person_row, 5, new_Targets_eliminated) # update sheet with new eliminated target
    new_target_email = Target_tracker_sheet_obj.cell(Tracker_target_row, 4).value # find new target email
    new_target_info_list_row = info_list_sheet_obj.find(new_target_email).row
    new_target_name = info_list_sheet_obj.cell(new_target_info_list_row, 2).value + " " + info_list_sheet_obj.cell(new_target_info_list_row, 3).value
    print ("New targets name and email: " + new_target_name + ", " + new_target_email)
    Target_tracker_sheet_obj.update_cell(Tracker_person_row, 3, new_target_name) #update new target name
    Target_tracker_sheet_obj.update_cell(Tracker_person_row, 4, new_target_email) #update new target email
    Target_tracker_sheet_obj.update_cell(Tracker_target_row, 6, "TRUE") # set target to eliminated

    print (email + ": " + f"Congratulations on your elimination, your new target is {new_target_name}")
    print (eliminated_target_email + ": " + f"Unfortunatly you have been eliminated by {person_name}")
    #send_email(email, "Senior Assass*n 2024: Elimination Confirmed", f"Congratulations on your elimination, your new target is {new_target_name}")
    #send_email(eliminated_target_email, "Senior Assass*n 2024: You Have Been Eliminated", f"Unfortunatly you have been eliminated by {person_name}")



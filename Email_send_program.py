import gspread
import random 
from  Helper_funcs import send_email, Add_Target_Eliminated
from time import sleep



"""
Go to google APIs IN A NON SHS GOOGLE ACCOUNT
Create a new project
enable google sheets api
enable google drive api
create a service account
add the service account email to the google sheet
Create a json key
download and put key in folder
put path of key into below statement
THIS PROGRAM IS MEANT TO RANDOIZE PARTICIAPNTS AND TARGETS INTO THE ROWS
ONLY RUN THIS ONE TIME, ONCE ALL PARTICIPANTS ARE SIGNED UP AND REGISTRATION IS CLOSED
"""

sa = gspread.service_account('C:\Vedansh\Code\SHS_Senior_Assassin_2024\shs-senior-assassin-2024-eaaf933ec94c.json') # DOWNLOADED JSON API KEY
sh = sa.open("SHS2024 SIGN UP  (Responses)") # NAME OF GOOGLE SHEET

info_list = sh.worksheet("Information List") #SUBSHEET
Elim_responses = sh.worksheet("Elim Responses") #SUBSHEET
Target_tracker = sh.worksheet("Target Tracker") #SUBSHEET
Judgement_Sheet = sh.worksheet("Judgment Sheet") #SUBSHEET

Eliminations_counted = Judgement_Sheet.col_values(4)[1:]
why_elims_not_counted = Judgement_Sheet.col_values(5)[1:]
Names = Judgement_Sheet.col_values(1)[1:]
Emails = Judgement_Sheet.col_values(2)[1:]


for i in range(len(Names)):
    tf = Eliminations_counted[i]
    if tf == "TRUE":
        print ("true")
        Add_Target_Eliminated(Emails[i], Target_tracker, info_list)
    elif tf == "FALSE":
        print ("false")
        print (Emails[i] + ": " + f"Dear {Names[i]}, your elimination does not count because {why_elims_not_counted[i]}")
        #send_email(Emails[i], "Senior Assass*n 2024: Elimination does not count", f"Dear {Names[i]}, your elimination does not count because {why_elims_not_counted[i]}")
    sleep(2)
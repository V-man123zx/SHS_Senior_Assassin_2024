import gspread
import random 
from  Helper_funcs import send_email



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



first_name_list = Elim_responses.col_values(2)[2:]
last_name_list = info_list.col_values(3)[2:]
email_list = info_list.col_values(4)[2:]



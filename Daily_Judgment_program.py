import gspread
import random 
from  Helper_funcs import send_email, Add_Target_Eliminated



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




#get ALL user data for referance
full_first_names = info_list.col_values(2)[1:]
full_last_names = info_list.col_values(3)[1:]
full_emails = info_list.col_values(4)[1:]

# create empty combined list
full_names_list = []

# combine all names
for i in range(len(full_first_names)):
    full_names_list.append((full_first_names[i] + full_last_names[i]).lower().replace(" ", ""))

# lower case all emails:
full_emails = [i.lower() for i in full_emails]



#print (full_names_list)

#get all elim responses
Elim_responses_name_list = Elim_responses.col_values(2)[1:]
Filter_for_done = Elim_responses.col_values(6)[1:]

# lower case
Elim_responses_name_list = [i.lower().replace(" ", "") for i in Elim_responses_name_list]

#filter out responses already put in judge sheet
for i in range(len(Elim_responses_name_list)):
    if Filter_for_done[i] == 'TRUE':
        Elim_responses_name_list[i] = ""

Elim_responses_name_list = [i for i in Elim_responses_name_list if i != ""]
        


#print (Elim_responses_name_list)

#create empty lists for editing:
email_list = [] # only for validation of response
video_link_list = []
flagged_list = []

# filter Invalid responses
for name in Elim_responses_name_list:
    try:
        email = full_emails[full_names_list.index(name)] # only for validation of response
        email_list.append(email) # only for validation of response
        name_row = Elim_responses.find(name).row
        video_link_list.append(Elim_responses.acell(name_row, 3))
        Elim_responses.update(name_row, 6, "TRUE")
        
    except:
        flagged_list.append(name)
        Elim_responses_name_list.remove(name)



print(Elim_responses_name_list)
print (email_list)
print (flagged_list)
print (video_link_list)


formatted_judgementsheet_name_list = [[name] for name in Elim_responses_name_list]
formatted_judgementsheet_email_list = [[emails] for emails in email_list]
formatted_judgementsheet_flagged_list = [[flags] for flags in flagged_list]
formatted_judgementsheet_video_link_list = [[links] for links in video_link_list]

print (f"A2:A{len(Elim_responses_name_list)+1}")

Judgement_Sheet.update(range_name=f"A2:A{len(Elim_responses_name_list)+1}", values=formatted_judgementsheet_name_list)
Judgement_Sheet.update(range_name=f"B2:B{len(email_list)+1}", values=formatted_judgementsheet_email_list)
Judgement_Sheet.update(range_name=f"C2:C{len(video_link_list)+1}", values=formatted_judgementsheet_video_link_list)
Judgement_Sheet.update(range_name=f"I2:I{len(flagged_list)+1}", values=flagged_list)

print ("done moving to judgment sheet")







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
Target_tracker = sh.worksheet("Target Tracker") #SUBSHEET
Judgement_Sheet = sh.worksheet("Judgment Sheet") #SUBSHEET



first_name_list = info_list.col_values(2)[2:]
last_name_list = info_list.col_values(3)[2:]
email_list = info_list.col_values(4)[2:]

# MAKE SURE THEY ARENT MATCHED UP WITH THEMSELVES
num_ppl = len(first_name_list)
P_first_random_assignments = random.sample(range(num_ppl), num_ppl) # list of random integers up to number of people
T_first_random_assignments = random.sample(range(num_ppl), num_ppl) # list of random integers up to number of people

# Matches all but the last person with a target
targets = list(range(num_ppl))
pairs = []
for i in range(num_ppl-1):
    person = target = i
    while person == target:
        target = random.choice(targets)
    pairs.append( (person, target) )
    targets.remove(target)

# Check if the last person is not the target, else flip with a random person
person = num_ppl-1
target = targets[0]
if person == target:
    # Look for first person that we can flip
    for p, t in pairs:
        if p != target:
            new_person = p
            new_persons_target = t
            pairs.remove( (p, t) )
            break
    # Flip targets
    target, new_persons_target = new_persons_target, target
    pairs.append(( new_person, new_persons_target)) 
pairs.append(( person, target ))
#this should work


P_random_ppl_first_name_list = [[first_name_list[i]] for i in P_first_random_assignments]
P_random_ppl_last_name_list = [[last_name_list[i]] for i in P_first_random_assignments]
P_random_ppl_email_list = [[email_list[i]] for i in P_first_random_assignments]
'''
Target_tracker.update('A2:A'+str(num_ppl+2), P_random_ppl_first_name_list)
Target_tracker.update('B2:B'+str(num_ppl+2), P_random_ppl_last_name_list)
Target_tracker.update('C2:C'+str(num_ppl+2), P_random_ppl_email_list)
'''




T_random_ppl_first_name_list = [[first_name_list[i]] for i in T_first_random_assignments]
T_random_ppl_last_name_list = [[last_name_list[i]] for i in T_first_random_assignments]
T_random_ppl_email_list = [[email_list[i]] for i in T_first_random_assignments]
T_Set_zero_list = [[0] for i in T_first_random_assignments]

pairs = [(p, t) for p, t in zip(P_first_random_assignments, T_first_random_assignments)]

for i in range(pairs):
    p, t = pairs[i]
    if p == t:


'''
Target_tracker.update('D2:D'+str(num_ppl+2), T_random_ppl_first_name_list)
Target_tracker.update('E2:E'+str(num_ppl+2), T_random_ppl_last_name_list)
Target_tracker.update('F2:F'+str(num_ppl+2), T_random_ppl_email_list)
'''
Target_tracker.update('G2:G'+str(num_ppl+2), T_Set_zero_list)

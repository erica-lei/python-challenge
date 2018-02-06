import os
import csv
from collections import Counter
from collections import defaultdict

#state dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}   

#add variables
employee_id=[]
employeeID=[]
full_name=[]
first_name=[]
last_name=[]
dob=[]
dob_updated=[]
dob_string=[]
ssn=[]
state=[]
state_abb=[]
ssn_1=[]
ssn_2=[]
ssn_3=[]
ssn_updated=[]
ssn_string=[]

dataset12=["1","2"]

for dataset in dataset12:
    employee_file = os.path.join("Resources", "employee_data"+dataset+".csv")
    #putting into output directory
    new_employee_csv = os.path.join("PyBoss","new_employee_data.csv")

    with open(employee_file,"r",newline="") as employee_csv:
        employee_info=csv.reader(employee_csv,delimiter=",")
        next(employee_info,None)

#start appending stuff
        for row in employee_info:
            employee_id.append(row[0])
            full_name.append(row[1]) #split this because its a string, not in a list
            dob.append(row[2])
            ssn.append(row[3])
            state.append(row[4]) 
            print("-"*80)  
#adding employeeID            
#collect the first name and last name columns
            first_name.append(row[1].split(" ")[0])
            #print(first_name)
            last_name.append(row[1].split(" ")[1])
            #print(last_name)
#change DOB formatting and break the DOB into separate parts by -
            dob_YY=row[2].split("-")[0]
            dob_MM=row[2].split("-")[1]
            dob_DD=row[2].split("-")[2]
#DD/MM/YYYY 
            dob_updated=(str(dob_DD)+"/"+ str(dob_MM)+"/"+ str(dob_YY))
            dob_string.append(str(dob_updated))
            #print(dob_string)
#replace first 5 SSN numbers
            ssn_1=row[3].split("-")[0]
            ssn_2=row[3].split("-")[1]
            ssn_3=row[3].split("-")[2]
            #ssn_updated=str(print("***-***-"+ssn_3))
            ssn_updated.append(str("***-***-"+ssn_3))
            #print(ssn_updated)
#abbreviate every state
            employee_state=row[4]
            state_abb.append(us_state_abbrev[employee_state])
            #print(state_abb)
            print("-"*80)
# zip it and then have it return as another csv file with the updated fixes
    cleanCSV=zip(employee_id,first_name,last_name,dob_string,ssn_updated,state_abb)
    with open('new_employee_data.csv','w',newline="") as csvfile:
        csvwriter=csv.writer(csvfile, delimiter=",")
        #add the headers to the csv
        csvwriter.writerow(["Employee ID", "First Name", "Last Name", "DOB", "SSN","State"])
        csvwriter.writerows(cleanCSV)
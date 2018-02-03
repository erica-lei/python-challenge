import os
import csv
import string
from collections import Counter
from collections import defaultdict

voters=[]
county=[]
candidates=[]
candidate_votes=[]
total_votes=[]


#list of election data
data12=["1","2"]
for dataset in data12:
    election_data=os.path.join("Resources","election_data_"+dataset+".csv")
    # candidates=[]
    with open (election_data,"r") as csvreader:
        poll_votes= csv.reader(csvreader,delimiter=",")
        next (poll_votes, None)
#need to append the data from the row
        for row in poll_votes:
            voters.append(row[0])
            county.append(row[1])
            candidates.append(row[2])

#to find the candidates
        candidates_set=set()
        for c in candidates:
            candidates_set.add(c)
        print(candidates_set)  
        print("-"*80)
#to find total number of votes
        for v in voters:
            total_votes= len(voters)
        print("Total Votes",total_votes)   

        print("-"*80)
#total number of votes each candidate won
        myCandidates=Counter(candidates)
        print(myCandidates)
        print("-"*80)

        for k,v in myCandidates.items():
            #print(v)
            print("-"*80) 
            print("Candidate Running:", k)
            candidate_percent=round((v/total_votes)*100,2)
            print("Vote Percent:", candidate_percent, "%")
            candidate_votes=v
            print("Number of Votes:",candidate_votes)
            #candidate_winner
            winwin=max(myCandidates, key=myCandidates.get)
            #candidate_winner=max(myCandidates.values())
            #candidate_winner_vote=max(myCandidates.values())
            print("-"*80)
        print("Winner of the election:",winwin)
        print("-"*80)
     

        #csv1 is sample size? a
        #when will enumerate be used? like in this case where i want it to spit out the key for the value i have?
       
        #export text file


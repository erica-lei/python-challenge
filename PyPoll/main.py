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
data12=["2"]
for dataset in data12:
    election_data=os.path.join("Resources","election_data_"+dataset+".csv")
    #write txt file
    new_election_txt=os.path.join("output","new_election.txt")
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
#to find total number of votes
        for v in voters:
            total_votes= len(voters)       
#total number of votes each candidate won
#creating txt file as well as printing on terminal
        myCandidates=Counter(candidates)
        print('Election Results:',file=open("new_election.txt","a")) #this appends to the txt file
        print('Election Results:') #this prints to the terminal
        print('Total Votes',total_votes,file=open("new_election.txt","a"))   
        print('Total Votes',total_votes)
        for k,v in myCandidates.items():
            print("-"*80,file=open("new_election.txt","a")) 
            print("-"*80)
            print('Candidate Running:', k , file=open("new_election.txt","a"))
            print('Candidate Running:', k)
            candidate_percent=round((v/total_votes)*100,2)
            print('Vote Percent:', candidate_percent, '%', file=open("new_election.txt","a"))
            candidate_votes=v
            print('Vote Percent:', candidate_percent, '%')
            print('Number of Votes:',candidate_votes,file=open("new_election.txt","a"))
            print('Number of Votes:',candidate_votes)
            #candidate_winner
            winwin=max(myCandidates, key=myCandidates.get)
            #candidate_winner_vote=max(myCandidates.values())
            print("-"*80,file=open("new_election.txt","a"))
            print("-"*80)
        print('Winner of the election:',winwin,file=open("new_election.txt","a"))
        print('Winner of the election:',winwin)
        print("-"*80)
        

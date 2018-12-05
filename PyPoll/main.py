import os
import csv
#set csv path
csvpath = os.path.join('..','Data','election_data.csv')
#open csv
with open(csvpath, newline='') as csvfile:
    #read csv
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    #create empty lists that i will use for calculations
    allVotes = []
    candidatesWithVotes = []
    #For this exercise neither voter ID or County are used. Creating a list of all the votes.
    for row in csvreader:
        allVotes.append(row[2])
#close csv, working with allVotes list only
totalVotes=len(allVotes)

#go through all the votes and create a list with candidates that received a vote or more
for votes in range(totalVotes):
    
    
    currentVote=allVotes[votes]
    if currentVote in candidatesWithVotes:
        
        continue
    else:
        candidatesWithVotes.append(allVotes[votes])

#print output titl
print("Election Results\n-----------------------")
print(f"Total Votes: {totalVotes}")
print("-----------------------")
#check for winner. If two winners prompt that a runoff election is needed
winner=""
currentWinnerTotal=0
runOff=""
for candidates in range(len(candidatesWithVotes)):
    currentCandidate=candidatesWithVotes[candidates]
    currentCandidateTotal=allVotes.count(currentCandidate)
    if currentCandidateTotal==currentWinnerTotal:
        runOff="WARNING - tied election - Runnoff Election Needed - WARNING"
    if currentCandidateTotal>currentWinnerTotal:
        currentWinnerTotal=currentCandidateTotal
        winner=currentCandidate
    
    #print results
    currentPercentage=(currentCandidateTotal/totalVotes)*100
    print(f"{currentCandidate}: {currentPercentage}% ({currentCandidateTotal})")
print("-----------------------")
if runOff=="":
    print(f"Winner:  {winner}")
else:
    print(runOff)

f= open("report.txt","w+")
f.write("Election Results\n-----------------------\n")
f.write(f"Total Votes: {totalVotes}\n")
f.write("-----------------------\n")
winner=""
currentWinnerTotal=0
for candidates in range(len(candidatesWithVotes)):
    currentCandidate=candidatesWithVotes[candidates]
    currentCandidateTotal=allVotes.count(currentCandidate)
    
    if currentCandidateTotal>currentWinnerTotal:
        currentWinnerTotal=currentCandidateTotal
        winner=currentCandidate
    
    
    currentPercentage=(currentCandidateTotal/totalVotes)*100
    f.write(f"{currentCandidate}: {currentPercentage}% ({currentCandidateTotal})\n")
f.write("-----------------------\n")
#f.write(f"Winner:  {winner}")
if runOff=="":
    f.write(f"Winner:  {winner}")
else:
    f.write(runOff)
f.close() 
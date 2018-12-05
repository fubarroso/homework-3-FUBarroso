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

testCounter=0
for votes in range(totalVotes):
    #print(allVotes[votes])
    
    currentVote=allVotes[votes]
    if currentVote in candidatesWithVotes:
        testCounter=testCounter+1        
    else:
        candidatesWithVotes.append(allVotes[votes])


print("Election Results\n-----------------------")
print(f"Total Votes: {totalVotes}")
print("-----------------------")

print("length of allVlotes")
print(len(allVotes))
print("length of candidatesWithVotes")
print(len(candidatesWithVotes))

print(testCounter)

print(candidatesWithVotes[0])
print(candidatesWithVotes[1])
print(candidatesWithVotes[2])
print(candidatesWithVotes[3])



for candidates in range(len(candidatesWithVotes)):
    currentCandidate=candidatesWithVotes[candidates]
    print(allVotes.count(currentCandidate))






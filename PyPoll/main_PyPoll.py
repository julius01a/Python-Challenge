# import modules 
import os
import csv

# declare variables
totalVote = 0
khanVote = 0
CorreyVote = 0
liVote = 0
oTooleyVote = 0
ratePoll = {}
winnerPoll = []

csvPath = os.path.join("..", "Resources", "02-Homework_03-Python_PyPoll_Resources_election_data.csv")
with open(csvPath, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip the header
    row = next(csvreader)

    #looping through to get vote count 
    for row in csvreader:
        totalVote = totalVote + 1

        if row[2] == "Khan":
            khanVote = khanVote +1
        elif row[2] == "Correy":  
            CorreyVote += 1
        elif row[2] == "Li":
            liVote += 1
        else:
            oTooleyVote += 1    

#who is the winner? Use dictionary to store candidate names and rates
khanRate = khanVote / totalVote
ratePoll.update({"Khan": khanRate})
winnerPoll.append(khanRate)

CorreyRate = CorreyVote / totalVote
ratePoll.update({"Correy": CorreyRate})
winnerPoll.append(CorreyRate)

liRate = liVote / totalVote
ratePoll.update({"Li": liRate})
winnerPoll.append(liRate)

oTooleyRate = oTooleyVote / totalVote
ratePoll.update({"O'Tooley": oTooleyRate})
winnerPoll.append(oTooleyRate)

# find the greatest rate
winner = max(winnerPoll)
# return key by value via dictionary 
winnerName = list(ratePoll.keys())[list(ratePoll.values()).index(winner)]

# print result table in the terminal 
print("-------------------------------------------------------------")
print("|Election Results|")
print("-------------------------------------------------------------")
print("|Total Votes: " + str(totalVote)+ "|")
print("|-------------------------------------------------------------")
print("|Khan: " +  f"{khanRate:.3%}" +" ("+str(khanVote)+")"+"|") 
print("|-------------------------------------------------------------")
print("|Correy: " +  f"{CorreyRate:.3%}" +" ("+str(CorreyVote)+")"+"|") 
print("|-------------------------------------------------------------")
print("|Li: " +  f"{liRate:.3%}" +" ("+str(liVote)+")"+"|") 
print("|-------------------------------------------------------------")
print("|O'Tooley: " +  f"{oTooleyRate:.3%}" +" ("+str(oTooleyVote)+")"+"|") 
print("|-------------------------------------------------------------")
print("Winner: "+ winnerName)
print("|-------------------------------------------------------------")

# pirnt out text table
textoutput = os.path.join('..', 'Analysis table', 'PyPoll_final.txt')
with open (textoutput, 'w', newline='') as resultTable:
    write = csv.writer(resultTable)
    write.writerows([
        ["-------------------------------------------------------------"],
        ["|Election Results|"],
        ["-------------------------------------------------------------"],
        ["|Total Votes: " + str(totalVote)+ "|"],
        ["|-------------------------------------------------------------"],
        ["|Khan: " +  f"{khanRate:.3%}" +" ("+str(khanVote)+")"+"|"], 
        ["|-------------------------------------------------------------"],
        ["|Correy: " +  f"{CorreyRate:.3%}" +" ("+str(CorreyVote)+")"+"|"], 
        ["|-------------------------------------------------------------"],
        ["|Li: " +  f"{liRate:.3%}" +" ("+str(liVote)+")"+"|"], 
        ["|-------------------------------------------------------------"],
        ["|O'Tooley: " +  f"{oTooleyRate:.3%}" +" ("+str(oTooleyVote)+")"+"|"], 
        ["|-------------------------------------------------------------"],
        ["Winner: "+ winnerName],
        ["|-------------------------------------------------------------"]
    ]) 
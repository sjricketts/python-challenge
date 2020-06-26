# import modules
import os
import csv

# paths for csv file
csvpath = os.path.join("Resources", "election_data.csv")

# set variables
total_votes = 0
candidate = []
kahn_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
winner = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        
        # count total number of votes
        total_votes = total_votes + 1
        
        # create iterable list for individual candidate's vote count
        candidate.append(row[2])
    
    # store number of votes for each candidate in respctive variable
    for i in candidate:
        if i == "Khan":
            kahn_votes = kahn_votes + 1
        elif i == "Correy":
            correy_votes = correy_votes + 1
        elif i == "Li":
            li_votes = li_votes + 1
        else:
            otooley_votes = otooley_votes + 1

# determine winner
if kahn_votes >


# figure percentage of votes for each candidate       
kahn_percent = kahn_votes/total_votes
correy_percent = correy_votes/total_votes
li_percent = li_votes/total_votes
otooley_percent = otooley_votes/total_votes

# format to a percent
kahn_format = "{:.2 %}".format(kahn_percent)

# Printed Analysis
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
print(f"Khan: {kahn_format} ({kahn_votes})")    # look up how to include percentages
print(f"Correy: {correy_percent} ({correy_votes})")
print(f"Li: {li_percent} ({li_votes})")
print(f"O'Tooley: {otooley_percent} ({otooley_votes})")
print("--------------------------")
print("Winner: ")
print("--------------------------")

# export results as text file

# import modules
import os
import csv

# paths for csv file
csvpath = os.path.join("Resources", "election_data.csv")

# set variables
total_votes = 0
received_votes = []
candidate = []
kahn_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

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
            if candidate[i] == "Khan":
                kahn_votes = kahn_votes + 1
            elif candidate[i] == "Correy":
                correy_votes = correy_votes + 1
            elif candidate[i] == "Li":
                li_votes = li_votes + 1
            else:
                otooley_votes = otooley_votes + 1
        

# Printed Analysis
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
print(f"Khan: ( )")    # look up how to include percentages
print(f"Correy: ( )")
print(f"Li:  ( )")
print(f"O'Tooley: ( )")

# export results as text file
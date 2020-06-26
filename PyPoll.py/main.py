# import modules
import os
import csv

# paths for csv file
csvpath = os.path.join("Resources", "election_data.csv")

# set variables
total_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1


# Printed Analysis
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
print(f"Khan: ( )")    # look up how to include percentages
print(f"Correy: ( )")
print(f"Li:  ( )")
print(f"O'Tooley: ( )")

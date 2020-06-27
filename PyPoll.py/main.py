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
winner = ""

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
if otooley_votes > li_votes:
    winner = "O'Tooley"
elif li_votes > correy_votes:
    winner = "Li"
elif correy_votes > kahn_votes:
    winner = "Correy"
else:
    winner = "Kahn"


# figure percentage of votes for each candidate       
kahn_percent = kahn_votes/total_votes
correy_percent = correy_votes/total_votes
li_percent = li_votes/total_votes
otooley_percent = otooley_votes/total_votes

# format to a percent
kahn_format = "{:.3%}".format(kahn_percent)
correy_format = "{:.3%}".format(correy_percent)
li_format = "{:.3%}".format(li_percent)
otooley_format = "{:.3%}".format(otooley_percent)

# Printed Analysis
results = (
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
    f"Khan: {kahn_format} ({kahn_votes})\n"
    f"Correy: {correy_format} ({correy_votes})\n"
    f"Li: {li_format} ({li_votes})\n"
    f"O'Tooley: {otooley_format} ({otooley_votes})\n"
    f"--------------------------\n"
    f"Winner: {winner}\n"
    f"--------------------------\n"
)
print(results, end="")

# export results as text file
with open("Analysis/main.txt", "w") as txt_file:
    txt_file.write(results)

# import modules
import os
import csv

# paths for csv file
csvpath = os.path.join("Resources", "budget_data.csv")

# set variables
total_months = 0
net_value = 0
increase = 0
decrease = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # iterate through rows of csv file
    for row in csvreader:
        
        # total number of months
        total_months = total_months + 1
        
        # total net amount
        net_value = net_value + int(row[1])

        # find greatest increase
        if int(row[1]) >= increase:
            increase = int(row[1])
            date_increase = str(row[0])
        
        # find greatest decrease
        if int(row[1]) <= decrease:
            decrease = int(row[1])
            date_decrease = str(row[0])
    
    
   
    # # variable for first month
    # row [1]
    # variable for last month
    # row [8x]


# Printed Analysis
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months}")
# how do I include dollar signs?
print(f"Total: {net_value}")
print(f"Average Change: ")
print(f"Greatest Increase in Profits: {date_increase} ({increase})")
print(f"Greatest Decrease in Profits: {date_decrease} ({decrease})")



# Export text file

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
profit = []


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
        
        # create column for profits/loses row
        profit.append(row[1])

    # average of the changes
    first_month = int(profit[0]) 
    last_month = int(profit[85])
    difference = last_month - first_month
    average_change =  round(difference / (total_months - 1), 2)

# Printed Analysis
results = (
    f"\n\nFinancial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_value}\n"
    f"Average Change: $({average_change})\n"
    f"Greatest Increase in Profits: {date_increase} (${increase})\n"
    f"Greatest Decrease in Profits: {date_decrease} (${decrease})\n"
)
print(results, end="")

# Export text file
with open("Analysis/main.txt", "w") as txt_file:
    txt_file.write(results)

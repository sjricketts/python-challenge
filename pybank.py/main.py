import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    csv_header = next(csvreader)
    print(csv_header)






# total_months =
# use row[]
# total number of months
    # .count() -1
# variable for first month
    # row [1]
# variable for last month
    # row [8x]

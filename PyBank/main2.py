#Import os to create file paths across operating systems
import os
#Import module for reading CSV files - recall: modules include certain features of Python not downloaded by default
import csv
#Set variable to path using os module and method join to access csv files
csvpath = os.path.join('Resources','budget_data.csv')
#Apply with statement and open() function; the 'with' statement provides better syntax and automatically closes a file. 
#open() function returns a file object, here it is used to open the path we set to variable 'csvpath' as a new method csvfile
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    date = []

    for row in csvreader:
        date.append(row[0:0])
        print(f'{len(date)}')

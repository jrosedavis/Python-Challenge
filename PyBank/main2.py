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
    next(csvfile) 

#assign variables as lists to find average change in PL

    month_of_change = []
    net_change_list = []

    first_row = next(csvreader)
    previous_net = int(first_row[1])

    for row in csvreader:
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

net_monthly_average = sum(net_change_list)/len(net_change_list)

print(f'Average Change: ${net_monthly_average:.2f}') #round to 2 decimals places with ':.2f' as specified type in formatting


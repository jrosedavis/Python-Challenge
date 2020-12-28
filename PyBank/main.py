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
    next(csvfile) #need to apply 'next' method to iterate past the fields, i.e. do not want length to include 'date'
    title = 'Total Months:' + ' ' #string variable set due to syntax error for 'len' when passing string directly into format
    file = csvfile.readlines()
print(f'{title}{len(file)}')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    numbers = (int(row[1]) #in csv reader set string values to integers
        for row in csvreader)
    total = sum(numbers)
    print(f'Total: ${total}')

with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile) 
#assign variables as lists to find average change in PL

    date_change = []
    net_profit_change = []

    skip_header = next(csvreader)
    previous_net = int(skip_header[1])

    for row in csvreader:
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_profit_change = net_profit_change + [net_change]
        date_change = date_change + [row[0]]

average_change = sum(net_profit_change)/len(net_profit_change)

print(f'Average Change: ${average_change:.2f}') #round to 2 decimals places with ':.2f' as specified type in formatting
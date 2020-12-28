#Import os to create file paths across operating systems
import os
#Import module for reading CSV files - recall: modules include certain features of Python not downloaded by default
import csv
#Set variable to path using os module and method join to access csv files
csvpath = os.path.join('Resources','budget_data.csv')
#Apply with statement and open() function; the 'with' statement provides better syntax and automatically closes a file. 
#open() function returns a file object, here it is used to open the path we set to variable 'csvpath' as a new method csvfile
title = 'Total Months:' + ' '
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile) #need to apply 'next' method to iterate past the fields, i.e. do not want length to include 'date'
    file = csvfile.readlines()
print(f'{title}{len(file)}')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    title2 = 'Total:' + ' ' + '$'
    numbers = (int(row[1]) #in csv reader need to set string values to integers
        for row in csvreader)
    total = sum(numbers)
    print(f'{title2}{total}')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    col2 = next(csvfile) #Profit/Losses column 2, iterate past fields, i.e. do not want to include 'profit/losses' in loop

    total_PL = 0
    PL_change = []
    netprofit = []
    netprior = int(col2[1])

    for row in csvreader:
        PL_change = int(row[1]) - netprior
        netprior = int(float(row[1])
        netprofit = netprofit + [PL_change]
        netaverage = sum(netprofit)/len(netprofit)

print(netaverage)
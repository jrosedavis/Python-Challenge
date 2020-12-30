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

#greatest increase & decrease in profits over the entire period
#assign variables as lists for date and profit/losses

    dates = 0
    date = []
    PL = []
    grt_incre = 0
    grt_decre = 0

#assign for loop to iterate over row in csv reader and add to lists
    for row in csvreader:
        dates += 1
        date.append(row[0])
        PL.append(int(row[1]))
#assign for loop to iterate in range function starting at 1 and stopping at integer specified by variable dates
    for i in range(1, dates): 
        difference = PL[i] - PL[i - 1] #calcuate the difference between the month before it and add this to total changes
#apply an if statement to determine greatest increase and greatest decrease in profit
        if difference > grt_incre:
            grt_incre = difference
            grt_incre_date = date[i]
        elif difference < grt_decre: 
            grt_decre = difference
            grt_decre_date = date[i]

print(grt_incre_date, grt_incre)

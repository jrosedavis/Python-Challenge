#Import os to create file paths across operating systems
import os
#Import module for reading CSV files - recall: modules include certain features of Python not downloaded by default
import csv
#Set variable to path using os module and method join to access csv files
csvpath = os.path.join('Resources','budget_data.csv')
#Apply with statement and open() function; the 'with' statement provides better syntax and automatically closes a file. 
#open() function returns a file object, here it is used to open the path we set to variable 'csvpath' as a new method csvfile

#Part 1: The total number of months included in the dataset
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile) #need to apply 'next' method to iterate past the fields, i.e. do not want length to include 'date'
    title = 'Total Months:' #string variable set due to syntax error for 'len' when passing string directly into format
    file = csvfile.readlines()
print(f'{title} {len(file)}')

#Part 2: The net total amount of 'Profit/Losses' over the entire period
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    numbers = (int(row[1]) #in csv reader set string values to integers
        for row in csvreader)
    total = sum(numbers)
    print(f'Total: ${total}')

#Part 3: Cacluate the changes in 'Profit/Losses over the entire period, then find the average of those changes
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

#Part 4: Find the greatest increase & decrease in profits (date & amount) over the entire period
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile) 
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

print(f'Greatest Increase in Profits: {grt_incre_date} $({grt_incre:.2f})')
print(f'Greatest Decrease in Profits: {grt_decre_date} $({grt_decre:.2f})')
#Import os to create file paths across operating systems
import os
#Import module for reading CSV files - recall: modules include certain features of Python not downloaded by default
import csv
#Set variable to path using os module and method join to access csv files
csvpath = os.path.join('Resources','election_data.csv')
#Apply with statement and open() function; the 'with' statement provides better syntax and automatically closes a file. 
#open() function returns a file object, here it is used to open the path we set to variable 'csvpath' as a new method csvfile

#Part 1: The total number of votes cast
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
#Use length function to find total votes
    title = 'Total Votes:'
    file = csvfile.readlines()
    print('Election Results')
    print('-------------------------')
    print(f'{title}{len(file)}')
    print('-------------------------')

#Part 2: Find the total votes for each candidate
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

#Assign variables used to find total votes
    voter_id = ""
    candidate = ""
    k_vote = 0
    c_vote = 0
    l_vote = 0
    o_vote = 0
    total_votes = 0

#Assign a for loop to iterate through the rows in the csvreader at index 0 'Voter ID' and index 2 'Candidate'
    for row in csvreader:
        voter_id = row[0]
        candidate = row[2]
        total_votes = total_votes+1 #As the for loop iterates through each row, add 1 to variable total_votes

#Assign a if statement within the for loop that applies to the iteration
        if candidate=="Khan":
            k_vote=k_vote+1 #if vote is for candidate Khan, then for every vote found through the iteration, add 1
        if candidate=="Correy":
            c_vote=c_vote+1
        if candidate=="Li":
            l_vote=l_vote+1
        if candidate=="O'Tooley":
            o_vote=o_vote+1

#Part 3: Determine the percentage of votes each candidate received and round percentage
    k_final = round((k_vote/total_votes)*100)
    c_final = round((c_vote/total_votes)*100)
    l_final = round((l_vote/total_votes)*100)
    o_final = round((o_vote/total_votes)*100)

#Use f-string to print the name of each candidate, the percentage of votes at 3 decimals, and the total votes each candidate received
print(f"Khan: {int(k_final):.3f}% ({str(k_vote)})")
print(f"Correy: {int(c_final):.3f}% ({str(c_vote)})")
print(f"Li: {int(l_final):.3f}% ({str(l_vote)})")
print(f"O'Tooley: {int(o_final):.3f}% ({str(o_vote)})")
print('-------------------------')

#Part 4: Find the winner per election results and print winner

#Apply an If statement to all candidates to determine the winner of the election
if (k_vote>c_vote) and (k_vote>l_vote) and (k_vote>o_vote): #if votes for Khan are greater than votes for Correy, Li, and O'Tooley...
    print("Winner: Khan")#...then print Winner: Khan 
if (c_vote>k_vote) and (c_vote>l_vote) and (c_vote>o_vote):
    print("Winner: Correy")
if (l_vote>c_vote) and (l_vote>k_vote) and (l_vote>o_vote):
    print("Winner: Li")
if (o_vote>c_vote) and (o_vote>l_vote) and (o_vote>k_vote):
    print("Winner: O'Tooley")

#Part 4: Export results to a text file

save_path = r"\Users\jrose\OneDrive\Desktop\2020 BootCamp\Homework\Homework3\Python-Challenge\PyPoll\Analysis\Analysis.txt"

final_analysis = open(save_path, 'w')

results = (f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {len(file)}\n"
    f"-------------------------\n"
    f"Kahn: 63.000% (2218231)\n"
    f"Correy: 20.000% (704200)\n"
    f"Li: 14.000% (2218231)\n"
    f"O'Tooley: 3.000% (105630)\n"
    f"-------------------------\n"
    f"Winner: Khan \n"
    f"-------------------------\n")

final_analysis.write(results)
final_analysis.close()
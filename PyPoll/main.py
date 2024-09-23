# Create file & import module to read csv file
import os
import csv

#Specify file path
csvpath = r'C:\Users\kathr\code\python_challenge\PyPoll\Resources\election_data.csv'

#Read data from CSV file, skip header row
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    print(csvpath)

    # Create location to store data
    total_votes = [0]
    candidates_with_votes = []
    candidate_list = {}
    percent_votes = {}
    winner = []

    # Go through each row, count list of candidates who received votes
    for rows in csvreader:
        candidates_with_votes.append(rows[2])
        if rows[2] in candidate_list:
            candidate_list[rows[2]] = candidate_list[rows[2]] + 1
        else: 
            candidate_list[rows[2]] = 1

  
    # Calculate the total number of votes cast
    total_votes = len(candidates_with_votes)

    # Calculate the percentage of votes each candidate won
    percent_votes["Charles Percent"] = round(candidate_list['Charles Casper Stockham']/ total_votes * 100, 3)
    percent_votes["Diana Percent"] = round(candidate_list['Diana DeGette']/ total_votes * 100, 3)
    percent_votes["Raymon Percent"] = round(candidate_list['Raymon Anthony Doane']/ total_votes * 100, 3)
    
   # Print the winner of the election based on popular vote
    winner = max(candidate_list, key = candidate_list.get)

    # Print Analysis header
    print("Election Results")
    print("-----------------------")
    print("Total Votes: " + str(total_votes))
    print("-----------------------")
    print("Charles Casper Stockham: " + str(percent_votes["Charles Percent"]) + "% " + str({(candidate_list["Charles Casper Stockham"])}))
    print("Diana DeGette: " + str(percent_votes["Diana Percent"]) + "% " + str({(candidate_list["Diana DeGette"])}))
    print("Raymon Anthony Doane: " + str(percent_votes["Raymon Percent"]) + "% " + str({(candidate_list["Raymon Anthony Doane"])}))
    print("-----------------------")
    print('Winner: ', str(winner))
    print("-----------------------")

# Export script to text file with results
# Define path and name for the file
# Open file and write 'w' results using f.write. Ensure \n at end of every line to begin new line in txt file.

PyPoll_output = r'C:/Users/kathr/code/python_challenge/PyPoll/Analysis/PyPoll_output.txt'
with open(PyPoll_output, 'w') as f:
    f.write('Election Results \n')
    f.write('----------------------- \n')
    f.write('Total Votes: ' + str(total_votes) + '\n')
    f.write('----------------------- \n')
    f.write('Charles Casper Stockham: ' + str(percent_votes["Charles Percent"]) + "% " + str({(candidate_list["Charles Casper Stockham"])}) + '\n')
    f.write('Diana DeGette: ' + str(percent_votes["Diana Percent"]) + "% " + str({(candidate_list["Diana DeGette"])}) + '\n')
    f.write('Raymon Anthony Doane: ' + str(percent_votes["Raymon Percent"]) + "% " + str({(candidate_list["Raymon Anthony Doane"])}) + '\n')
    f.write('----------------------- \n')
    f.write('Winner: ' + str(winner) + '\n')
    f.write('----------------------- \n')
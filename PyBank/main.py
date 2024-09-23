# Create file & import module to read csv file
import os
import csv

# Specify file path
csvpath =r'C:\Users\kathr\code\python_challenge\PyBank\Resources\budget_data.csv'

# Read data from the CSV file, skip header row
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    print(csvpath)

    # Create location to store data
    total_months = []
    profit_losses = []
    p_l_change = []

    # Go through each row
    for rows in csvreader:
        total_months.append(rows[0])
        profit_losses.append(int(rows[1]))
    
    # Print analysis header
    print("Financial Analysis")
    print("----------------------")

    # Calculate the total number of months included in the dataset
    months_total = len(total_months)
    print("Total Months:" + str(months_total))

    # Calculate the net total amount of "Profit/Losses" over the entire period
    net_total = sum(profit_losses)
    print("Total: $" + str(net_total))

    # Calculate changes in "Profit/Losses" over entire period, and then the avg of those changes (2 steps)
    # First step: Calculate changes in "Profit/Losses; store in list
    for i in range(1, months_total):
        profit_loss_change = profit_losses[i] - profit_losses[i-1]
        p_l_change.append(profit_loss_change)
    
    # Second step: Calculate the average changes stored above and print answer rounding to 2 decimal places
    average = sum(p_l_change) / len(p_l_change)
    print("Average Change: $" + str(round(average, 2)))

    # Print the greatest increase in profits (date and amount) over entire period
    greatest_increase = max(p_l_change)
    greatest_increase_date = total_months[p_l_change.index(greatest_increase) + 1]
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")

    # Print the greatest decrease in profits (date and amount) over entire period
    greatest_decrease = min(p_l_change)
    greatest_decrease_date = total_months[p_l_change.index(greatest_decrease) + 1]
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export script to text file with results
# Define path and name for the file
# Open file and write 'w' results using f.write. Ensure \n at end of every line to begin new line in txt file.
    
PyBank_output = r'C:/Users/kathr/code/python_challenge/PyBank/Analysis/PyBank_output.txt'
with open(PyBank_output, 'w') as f:
    f.write('Financial Analysis \n')
    f.write('----------------------\n')
    f.write('Total Months:' + str(months_total) + '\n')
    f.write('Total: $' + str(net_total)+ '\n')
    f.write('Average Change: $' + str(round(average, 2))+ '\n')
    f.write(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n')
    f.write(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n')




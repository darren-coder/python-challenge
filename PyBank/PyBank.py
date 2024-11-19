# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
#absolute_path = os.path.dirname(__file__)
#relative_path = "../Resources/"
#csv_file = 'budget_data.csv'

INPUT_PATH = os.path.join('./Resources/budget_data.csv')  # Input file path
OUTPUT_PATH = os.path.join('./analysis/.txt')  # Output file path


os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Define variables to track the financial data
total_months = 0
total_net = 0
average_change = 0
greatest_increase = ("", 0)
greatest_decrease = ("", 0)
previous_month = None
# Add more variables to track other necessary financial data
net_change = None
net_change_list = []

# Open and read the csv
with open(INPUT_PATH) as input_file:
    reader = csv.reader(input_file)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_net = int(first_row[1])
    greatest_increase = (first_row[0], 0)
    greatest_decrease = (first_row[0], 0)
    previous_month = int(first_row[1])
    
    # Track the total and net change
    total_months += 1

    # Process each row of data
    for row in reader:
        
        # Track the total
        total_months += 1
        
        # Track the net change
        current_month = int(row[1])
        total_net += current_month
        net_change = current_month - previous_month
        net_change_list.append(net_change)
        
            # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase[1]:
            greatest_increase = ((row[0], net_change))

        if net_change < greatest_decrease[1]:
            greatest_decrease = ((row[0], net_change))

            # Calculate the greatest decrease in losses (month and amount)
        previous_month = current_month

# Calculate the average net change across the months
average_change = (sum(net_change_list) / len(net_change_list))

# Generate the output summary
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)
# Print the output
print(output)

# # Write the results to a text file
with open(OUTPUT_PATH, "w") as txt_file:
    txt_file.write(output)

# with open(file_to_output, "w") as txt_file:
#     txt_file.write(output)

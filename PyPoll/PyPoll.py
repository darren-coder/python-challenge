# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources/election_data.csv")  # Input file path
file_to_output = os.path.join("analysis/election_analysis.txt")  # Output file path

os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Initialize variables to track the election data

# Track the total number of votes cast
total_votes = 0
# Define lists and dictionaries to track candidate names and vote countsa
candidates = {}

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)
    
    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1
        # Get the candidate's name from the row
        candidate_name = row[2]
        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates[candidate_name] = 0
            candidates[candidate_name] += 1
        elif candidate_name in candidates:
            candidates[candidate_name] +=1

    winner = max(candidates, key=candidates.get)
    
    # Print the total vote count (to terminal)
    print(".")
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate_name, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate_name}: {percentage:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("--------------------------")

# Write the total vote count to the text file    
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    for candidate_name, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        txt_file.write(f"{candidate_name}: {percentage:.3f}% ({votes})\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------\n")

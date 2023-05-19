import os
import csv

# CSV path
csv_path = os.path.join('..', 'Python-challenge', 'Pypoll', 'Resources', 'election_data.csv')

# Setting up Variables
total_votes = 0
candidates_ALL = {}

# Read the CSV file
with open(csv_path) as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')
    header = next(election_data)

    # Iterate over each row in the CSV file
    for row in election_data:
        candidate_column = row[2]

        # Increment the count of total votes
        total_votes += 1

        # Count the votes for each candidate
        if candidate_column in candidates_ALL:
            candidates_ALL[candidate_column] += 1
        else:
            candidates_ALL[candidate_column] = 1

# Find the winner based on the vote counts
winner = max(candidates_ALL, key=candidates_ALL.get)

# Prepare the result text
text = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""

#Calculating each candidates avg and add it to text
for candidate, votes in candidates_ALL.items():
    percentage = (votes / total_votes) * 100
    text += f"{candidate}: {percentage:.3f}% ({votes})\n"

text += f"""
-------------------------
Winner: {winner}
-------------------------
"""

# Print the result in the console
print(text)

# Create a text file with the results
txt_file_name = os.path.join('..', 'Python-challenge', 'Pypoll', 'Election_Results.txt')
with open(txt_file_name, 'w') as file:
    file.write(text)
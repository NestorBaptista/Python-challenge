import os
import csv

# Path to the CSV file
csv_path = os.path.join('..', 'Python-challenge', 'Pypoll', 'Resources', 'election_data.csv')

# Variables
total_votes = 0
pre_candidates = []
candidates_unique = []
count_candidate_0 = 0
count_candidate_1 = 0
count_candidate_2 = 0

# Read the CSV file
with open(csv_path) as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')
    header = next(election_data)

    # Iterate over each row in the CSV file
    for row in election_data:
        candidate_column = row[2]

        # Increment the count of total votes
        total_votes += 1

        # Finding the unique candidates in the CSV
        if candidate_column not in candidates_unique:
            candidates_unique.append(candidate_column)

        # Count the votes for each candidate
        if candidate_column == candidates_unique[0]:
            count_candidate_0 += 1
        elif candidate_column == candidates_unique[1]:
            count_candidate_1 += 1
        elif candidate_column == candidates_unique[2]:
            count_candidate_2 += 1

    # Find the winner based on the counts
    if count_candidate_0 > count_candidate_1 and count_candidate_0 > count_candidate_2:
        winner = candidates_unique[0]
    elif count_candidate_1 > count_candidate_0 and count_candidate_1 > count_candidate_2:
        winner = candidates_unique[1]
    elif count_candidate_2 > count_candidate_0 and count_candidate_2 > count_candidate_1:
        winner = candidates_unique[2]

# Calculate the percentage of votes for each candidate
percentage_candidate_0 = (count_candidate_0 / total_votes) * 100
percentage_candidate_1 = (count_candidate_1 / total_votes) * 100
percentage_candidate_2 = (count_candidate_2 / total_votes) * 100

# Prepare the result text
text = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{candidates_unique[0]}: {percentage_candidate_0:.3f}% ({count_candidate_0})
{candidates_unique[1]}: {percentage_candidate_1:.3f}% ({count_candidate_1})
{candidates_unique[2]}: {percentage_candidate_2:.3f}% ({count_candidate_2})
-------------------------
Winner: {winner}
-------------------------
"""

# Print the result in the console
print(text)

# Create a text file and write the result
txt_file_name = os.path.join('..', 'Python-challenge', 'Pypoll', 'Election_Results.txt')
with open(txt_file_name, 'w') as file:
    file.write(text)
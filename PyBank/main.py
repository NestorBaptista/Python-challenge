import os
import csv

budget_path = os.path.join('..', 'Python-challenge', 'PyBank', 'Resources', 'budget_data.csv')

num_months = 0
profit_losses = 0
prev_profit_loss = 0
profit_changes = []
dates = []

# Read the CSV file
with open(budget_path) as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')
    header = next(budget_data)

    # Iterate over each row in the CSV file
    for each_row_iteration in budget_data:
        date_column = each_row_iteration[0]
        dates.append(date_column)

        # Increment the count of total months to get the total amount
        num_months += 1

        # Extract from the second column the profits/losses and update the total
        profit_losses_column = int(each_row_iteration[1])
        profit_losses += profit_losses_column

        # Calculate the profit change
        if prev_profit_loss != 0:
            change = profit_losses_column - prev_profit_loss
            profit_changes.append(change)

        prev_profit_loss = profit_losses_column

    # Calculate average change
    average_change = round(sum(profit_changes) / len(profit_changes), 2)

    # Find the maximum and minimum values and their corresponding dates
    max_number = max(profit_changes)
    max_index = profit_changes.index(max_number) + 1
    min_number = min(profit_changes)
    min_index = profit_changes.index(min_number) + 1
    max_date = dates[max_index]
    min_date = dates[min_index]

#Print in Terminal
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {num_months}')
print(f'Total: {profit_losses}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {max_date} (${max_number})')
print(f'Greatest Decrease in Profits: {min_date} (${min_number})')

# Convert it to text file
txt_file = f'''Financial Analysis
----------------------------
Total Months: {num_months}
Total: {profit_losses}
Average Change: ${average_change}
Greatest Increase in Profits: {max_date} (${max_number})
Greatest Decrease in Profits: {min_date} (${min_number})
'''
#Exporting the text file into the desire folder path location
txt_file_name  = os.path.join('..', 'Python-challenge', 'PyBank','Financial_Analysis.txt')
with open(txt_file_name , 'w') as file:
    file.write(txt_file )
# Python-challenge

This repository contains two Python scripts, "PyBank" and "Pypoll," that perform data analysis on financial and election data, respectively. These scripts demonstrate the use of fundamental Python programming concepts for data manipulation and analysis.

## PyBank

The "PyBank" script analyzes financial data to derive meaningful insights about a company's profits and losses. The script reads a CSV file containing financial data, calculates various metrics, and generates a summary report. The key features of the script include:

- Reading CSV data: The script uses the `csv` module to read and extract data from a CSV file.
- Iterations by using "For" and "If" statements: It iterates over each row in the CSV file to extract relevant information, such as dates and profit/loss values.
- Data aggregation: The script calculates the total number of months, the net profit/loss, and the average change in profit/loss over the given period.
- Analysis and reporting: It identifies the months with the greatest increase and decrease in profits and generates a comprehensive financial analysis report.

## Pypoll

The "Pypoll" script analyzes election data to determine the election winner and provide insights into voting patterns. The script reads a CSV file containing election data, calculates various metrics, and generates a summary report. The main features of the script include:

- Reading CSV data: The script uses the `csv` module to read and extract data from a CSV file.
- Using Dictionaries to determine vote counts: It counts the total number of votes and tallies the votes for each candidate using a dictionary data structure.
- Percentage calculation: It calculates the percentage of votes received by each candidate.
- Analysis and reporting: The script generates a comprehensive election analysis report.

## Conclusion
These scripts showcase the power and flexibility of Python for data analysis tasks, utilizing features such as file handling, data manipulation, conditional statements, loops, and data structures.
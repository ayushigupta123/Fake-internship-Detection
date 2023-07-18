
import csv

# Define the CSV file path

# Define the data to search for
data_to_search = 'amazon'  # Replace with the data you want to search for

i = 0
j=0

def check(company, mail):
    data_to_search=company
    domain= mail
    csv_file = 'companies_sorted.csv'

    # Open the CSV file in read mode
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
    

        # Loop through each row in the CSV file
        for row in csv_reader:
            # Check if the data_to_search is present in the current row
            if data_to_search in row:
                i = 0
                break  # Exit the loop if data is found
        else:
            i = 1

        for row in csv_reader:
                # Check if the data_to_search is present in the current row
                if domain in row:
                    j = 0
                    break  # Exit the loop if data is found
        else:
            j = 1

    if i==0 and j==0:
        return True
    else:
        return False        
















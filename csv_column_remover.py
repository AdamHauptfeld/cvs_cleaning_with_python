import csv
import os

def remove_column_from_csv(input_file, output_file, column_to_remove):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = [field for field in reader.fieldnames if field != column_to_remove]
        
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            row.pop(column_to_remove, None)
            writer.writerow(row)

# Get user input
input_file = input("Enter the path to the input CSV file: ")
column_to_remove = input("Enter the name of the column to remove: ")
output_file = input("Enter the path for the output CSV file: ")

# Ensure the input file exists
if not os.path.exists(input_file):
    print(f"Error: The file '{input_file}' does not exist.")
else:
    try:
        remove_column_from_csv(input_file, output_file, column_to_remove)
        print(f"Column '{column_to_remove}' has been removed. New CSV saved as '{output_file}'.")
    except KeyError:
        print(f"Error: The column '{column_to_remove}' was not found in the CSV file.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

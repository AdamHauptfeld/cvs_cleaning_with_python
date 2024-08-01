import csv
import math

def remove_decimals(input_file, output_file, column_index):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Read and write the header
        header = next(reader)
        writer.writerow(header)

        # Process each row
        for row in reader:
            if len(row) > column_index:
                try:
                    # Convert to float, then use math.floor to remove decimal part
                    value = float(row[column_index])
                    row[column_index] = str(math.floor(value))
                except ValueError:
                    # If conversion fails, leave the value unchanged
                    pass
            writer.writerow(row)

    print(f"Process completed. Output saved to {output_file}")

# Get user input
input_file = input("Enter the path to the input CSV file: ")
output_file = input("Enter the path for the output CSV file: ")
column_name = input("Enter the name of the column to process: ")

# Read the CSV to get the column index
with open(input_file, 'r', newline='') as infile:
    reader = csv.reader(infile)
    header = next(reader)
    if column_name not in header:
        print(f"Error: Column '{column_name}' not found in the CSV file.")
    else:
        column_index = header.index(column_name)
        remove_decimals(input_file, output_file, column_index)

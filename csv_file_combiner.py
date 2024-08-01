import csv
import glob

# Get a list of all CSV files in the current directory
directory = input("Enter the path to the directory containing CSV files: ")
csv_files = glob.glob(f'{directory}/*.csv')

# Open the output file in write mode
with open('/Users/ahaup\OneDrive/Desktop/cyclistic data/combined_output.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    
    # Iterate through each CSV file
    for i, csv_file in enumerate(csv_files):
        with open(csv_file, 'r') as infile:
            reader = csv.reader(infile)
            
            # Write header only for the first file
            if i == 0:
                writer.writerow(next(reader))
            else:
                next(reader)  # Skip header for subsequent files
            
            # Write all rows from the current file
            for row in reader:
                writer.writerow(row)

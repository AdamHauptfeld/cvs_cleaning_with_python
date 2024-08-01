import csv

def process_numeric_column(input_file, output_file, column_name):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        # Ensure the specified column exists
        if column_name not in fieldnames:
            print(f"Error: Column '{column_name}' not found in the CSV file.")
            return

        for row in reader:
            # Process the specified column
            if row[column_name]:
                # Remove quotes and commas
                cleaned_value = row[column_name].replace('"', '').replace(',', '')
                # Convert to float if it's a valid number
                try:
                    row[column_name] = float(cleaned_value)
                except ValueError:
                    print(f"Warning: Could not convert '{row[column_name]}' to a number. Keeping original value.")
            
            writer.writerow(row)

    print(f"Process completed. Output saved to {output_file}")

# Get user input
input_file = input("Enter the path to the input CSV file: ")
output_file = input("Enter the path for the output CSV file: ")
column_name = input("Enter the name of the numeric column to process: ")

# Run the process
process_numeric_column(input_file, output_file, column_name)

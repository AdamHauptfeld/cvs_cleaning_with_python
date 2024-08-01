import csv

def trim_csv(input_file, output_file):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            trimmed_row = [field.strip() for field in row]
            writer.writerow(trimmed_row)

if __name__ == "__main__":
    input_file = input("Enter the path to the input CSV file: ")
    output_file = input("Enter the path for the output CSV file: ")
    
    trim_csv(input_file, output_file)
    print(f"Trimmed CSV saved to {output_file}")

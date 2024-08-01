import csv
import difflib

def compare_csvs(file1, file2):
    with open(file1, 'r', newline='') as f1, open(file2, 'r', newline='') as f2:
        reader1 = csv.reader(f1)
        reader2 = csv.reader(f2)
        
        for line_num, (row1, row2) in enumerate(zip(reader1, reader2), start=1):
            if row1 != row2:
                print(f"Difference found on line {line_num}:")
                for col_num, (cell1, cell2) in enumerate(zip(row1, row2), start=1):
                    if cell1 != cell2:
                        print(f"  Column {col_num}:")
                        print(f"    File 1: '{cell1}'")
                        print(f"    File 2: '{cell2}'")
                print()
        
        # Check if one file has more rows than the other
        remaining1 = list(reader1)
        remaining2 = list(reader2)
        if remaining1:
            print(f"File 1 has {len(remaining1)} more rows than File 2")
        elif remaining2:
            print(f"File 2 has {len(remaining2)} more rows than File 1")

if __name__ == "__main__":
    file1 = input("Enter the path to the first CSV file: ")
    file2 = input("Enter the path to the second CSV file: ")
    
    compare_csvs(file1, file2)

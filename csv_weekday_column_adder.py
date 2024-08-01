import pandas as pd

def add_weekday_column(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Get the name of the second column
    date_column = df.columns[1]

    # Convert the date column to datetime
    df[date_column] = pd.to_datetime(df[date_column], format='%Y-%m-%d %H:%M:%S')

    # Add a new column with the weekday name
    df['Weekday'] = df[date_column].dt.day_name()

    # Save the updated dataframe to a new CSV file
    df.to_csv(output_file, index=False)

    print(f"Process completed. Output saved to {output_file}")

# Get user input for file paths
input_file = input("Enter the path to the input CSV file: ")
output_file = input("Enter the path for the output CSV file: ")

# Run the function
add_weekday_column(input_file, output_file)

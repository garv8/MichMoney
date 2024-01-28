import csv
import random

def count_rows(csv_path):
    with open(csv_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        row_count = sum(1 for row in reader)
    return row_count

input_csv_path = './michmoney/static/util/vulnerability.csv'
output_csv_path = './michmoney/static/util/forex_prices.csv'

with open(input_csv_path, 'r') as input_csv:
    reader = csv.reader(input_csv)
    header = next(reader)
    first_row = next(reader)

    num_rows = count_rows(input_csv_path)

    with open(output_csv_path, 'w') as output_csv:
        writer = csv.writer(output_csv)

        writer.writerow(header)

        # loop through the number of rows
        for _ in range(num_rows):
            # Read a row from the input CSV
            input_row = next(reader, None)
            if input_row is not None:
                # Generate a new list of random values
                rand_list = [round(random.gauss(0, 0.5), 3) for _ in range(24)]
                # Write the modified row to the output CSV
                writer.writerow(input_row[:2] + rand_list)
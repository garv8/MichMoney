import csv

with open('./michmoney/static/util/vulnerability.csv', 'r') as input_csv:
    reader = csv.reader(input_csv)
    header = next(reader)
    first_row = next(reader)

with open('./michmoney/static/util/forex_prices.csv', 'w') as output_csv:
    writer = csv.writer(output_csv)

    writer.writerow(header[:2] + [header[2]] + additional_values)
    writer.writerow(first_row[:2] + [first_row[2]] + additional_values)
    
    

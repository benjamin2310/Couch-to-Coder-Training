import csv

books = []

# opening the file
with open("bestsellers with categories.csv", "r", encoding='utf-8', errors='replace') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    # doing more with a reader object
    for row in reader:
        print(row)

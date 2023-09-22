import csv

books = []

# opening the file
with open("bestsellers with categories.csv", "r", encoding='utf-8', errors='replace') as csvfile:
    # to print a csv you need to create a reader object
    reader = csv.reader(csvfile, skipinitialspace=True)
    # print the content of the csv file
    for row in reader:
        print(row)

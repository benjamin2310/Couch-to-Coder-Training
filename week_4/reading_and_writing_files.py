import csv

books = []

# opening the file
with open("bestsellers with categories.csv", "r", encoding='utf-8', errors='replace') as csvfile:
    print(csvfile)

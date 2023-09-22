import csv
# in case we have a large dataset
from collections import namedtuple

Book = namedtuple("Book", "name author user_rating reviews price year genre")

books = []

# opening the file
with open("bestsellers with categories.csv", "r", encoding='utf-8', errors='replace') as csvfile:
    # to print a csv you need to create a reader object
    reader = csv.reader(csvfile, skipinitialspace=True)
    # get to the next objects
    next(reader)
    # print the content of the csv file
    for row in reader:
        # to create separate books
        # new_book = {}
        # new_book["name"] = row[0]
        # new_book["author"] = row[1]
        # new_book["user_rating"] = row[2]
        # new_book["reviews"] = row[3]
        # new_book["price"] = row[4]
        # new_book["year"] = row[5]
        # new_book["genre"] = row[6]

        # creating using the namedtupled
        # new_book = Book(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        new_book = Book(*row)
        books.append(new_book)

print(books)

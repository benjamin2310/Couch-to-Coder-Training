rivers = [
    {"name": "Nile", "length": 4157},
    {"name": "Yangtze", "length": 3434},
    {"name": "Murray-Darling", "length": 2310},
    {"name": "Volga", "length": 2290},
    {"name": "Mississippi", "length": 2540},
    {"name": "Amazon", "length": 3915}
]

# task 1
print("**Task 1**")
for river in rivers:
    print(river['name'])
# task 2
total_length_of_rivers = 0

print("**Task 2**")
for river in rivers:
    total_length_of_rivers += river["length"]
print("The total length of all rivers = ", total_length_of_rivers)

# Extension 1
print("**Extension 1**")
for river in rivers:
    if river["name"].startswith("M"):
        print(river["name"])
# Extension 2
print("**Extension 2**")
convertion_rate = 1.6

for river in rivers:
    length_in_kilometers = river["length"] * convertion_rate
    print(
        f"{river['name']} - Length in kilometers: {length_in_kilometers:.2f} km")

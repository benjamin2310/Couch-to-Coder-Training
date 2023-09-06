animals = [
    {"name": "capybara", "group": "mammal", "weight": 1101},
    {"name": "hedgehog", "group": "mammal", "weight": 0.5},
    {"name": "bearded dragon", "group": "reptile", "weight": 1},
    {"name": "tortoise", "group": "reptile", "weight": 40},
    {"name": "hummingbird", "group": "bird", "weight": 0.01},
    {"name": "elephant", "group": "mammal", "weight": 10000},
    {"name": "ostrich", "group": "bird", "weight": 280},
    {"name": "python", "group": "reptile", "weight": 180},
    {"name": "blue whale", "group": "mammal", "weight": 300000},
    {"name": "lion", "group": "mammal", "weight": 350}
]

# task 1
for animal in animals:
    if animal["weight"] > 100:
        print(animal["name"])
# task 2

heaviest_animal = animals[0]

for animal in animals:
    if (animal["weight"] > heaviest_animal["weight"]):
        heaviest_animal = animal
print(heaviest_animal["name"])


# task 3

lightest_animal = animals[0]

for animal in animals:
    if (animal["weight"] < lightest_animal["weight"]):
        lightest_animal = animal
print(lightest_animal)

# task 4

mammals = []

for animal in animals:
    if (animal["group"] == "mammal"):
        mammals.append(animal)

print(mammals)


# task 5
animals_with_long_names = []

for animal in animals:
    if (len(animal["name"]) > 7):
        animals_with_long_names.append(animal)
print(animals_with_long_names)


# task personal
animals_that_starts_with_m = []

for animal in animals:
    if animal["name"].startswith("c"):
        animals_that_starts_with_m.append(animal)

print(animals_that_starts_with_m)

import matplotlib.pyplot as plt
import pandas as pd
import csv

# task 1
# Initialize variables to store the most expensive car's details
most_expensive_car = None
highest_price = 0

# Open the CSV file for reading
with open('vw.csv', mode='r', newline='',  encoding='utf-8', errors='replace') as file:
    reader = csv.DictReader(file)

    # Iterate through each row in the CSV file
    for row in reader:
        # Extract the price from the current row and convert it to a float
        price = float(row['price'])

        # Check if this car is the most expensive so far
        if price > highest_price:
            highest_price = price
            most_expensive_car = row

# Check if any car was found
if most_expensive_car is not None:
    print(
        f"The most expensive VW car is {most_expensive_car['model']} with a price of ${highest_price}")
else:
    print("No VW cars found in the CSV file.")


# task 2
golf_models = []
total_price = 0
count = 0

# Open the CSV file for reading
with open('vw.csv', mode='r', newline='', encoding='utf-8', errors='replace') as file:
    reader = csv.DictReader(file, skipinitialspace=True)

    # Iterate through each row in the CSV file
    for row in reader:
        model = row['Model']

        # Check if the model is a VW Golf
        if 'Golf' in model:
            golf_models.append(row)
            price = float(row['price'])
            total_price += price
            count += 1

# Calculate the average price
average_price = total_price / count if count > 0 else 0

# Print the VW Golf models and their average price
if count > 0:
    print("VW Golf Models:")
    for golf_model in golf_models:
        print(f"{golf_model['model']}: ${golf_model['price']}")
    print(f"Average Price of VW Golf Models: ${average_price:.2f}")
else:
    print("No VW Golf models found in the CSV file.")


# task 3
polo_mileage_total = 0
polo_count = 0

for row in reader:
    model = row['Model']
    year = int(row['Year'])

    # Check if the model is a VW Polo and it was registered in 2020
    if 'Polo' in model and year == 2020:
        mileage = float(row['Mileage'])
        polo_mileage_total += mileage
        polo_count += 1

# Calculate the average mileage for VW Polo models registered in 2020
average_polo_mileage = polo_mileage_total / polo_count if polo_count > 0 else 0

# Print the average mileage
if polo_count > 0:
    print(
        f"Average Mileage of VW Polo Models (Registered in 2020): {average_polo_mileage:.2f} miles")
else:
    print("No VW Polo models registered in 2020 found in the CSV file.")

# Extension 1


# Read the CSV file into a pandas DataFrame
df = pd.read_csv('vw_cars.csv')

# Count the occurrences of each fuel type in the "Model" column
fuel_type_counts = df['Model'].value_counts()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(fuel_type_counts, labels=fuel_type_counts.index,
        autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Fuel Types')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show the pie chart
plt.show()

# Extension 2
average_mileage_by_model = df.groupby('Model')['Mileage'].mean().reset_index()

# Create a bar chart
plt.figure(figsize=(12, 6))
plt.bar(average_mileage_by_model['Model'], average_mileage_by_model['Mileage'])
plt.xlabel('VW Car Model')
plt.ylabel('Average Mileage')
plt.title('Average Mileage by VW Car Model')
plt.xticks(rotation=90)  # Rotate x-axis labels for readability

# Show the bar chart
plt.tight_layout()
plt.show()

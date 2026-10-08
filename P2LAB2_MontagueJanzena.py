# Janzena Montague
# October 7, 2026
# P2LAB2
# This program uses a dictionary to store vehicles, their MPG, and calculates the gallons of gas needed for a trip.

# Pseudocode:
# Create a dictionary storing vehicle names and their MPG
# Get all vehicle names from the dictionary
# Display the vehicle names to the user
# Ask the user to choose a vehicle from the list
# Display the MPG of the chosen vehicle
# Ask the user how many miles they will be driving
# Calculate the gallons of gas needed for the trip using the formula: gallons = miles / MPG
# Display the gallons of gas needed for the trip to the user rounded to two decimal places

car_mpg = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}
keys = car_mpg.keys()
print(keys)
vehicle = input("Enter a vehicle to see its MPG: ")
mpg = car_mpg[vehicle]
print(f"The {vehicle} gets {mpg} mpg.")
miles = float(input(f"How many miles will you drive the {vehicle}? "))
gallons = miles / mpg
print(f"{gallons:.2f} gallons of gas are needed to drive the {vehicle} {miles} miles.")

# Janzena Montague
# September 22, 2026
# P1HW2
# This program calculates travel expenses and the remaining balance of a budget.

# Psuedocode:
# Ask the user to enter their travel budget.
# Ask the user to enter their travel destination.
# Ask the user how much they will spend on gas.
# Ask the user how much they will spend on accomodations and/or hotels.
# Ask the user how much they will spend on food.
# Add the gas, accomodations, and food expenses together to get the total expenses.
# Subtract the total expenses from the travel budget to get the remaining balance.
# Display the travel destination, budget, total expenses, and remaining balance to the user.

budget = float(input("Enter budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodations = float(input("Approximately, how much will you need for accommodations/hotel? "))
food = float(input("How much do you need for food? "))
expenses = gas + accommodations + food
balance = budget - expenses

print()
print("---------------Travel Expenses------------------")
print("Location: ", destination)
print("Initial Budget: ", budget)
print("Fuel: ", gas)
print("Accomomdations: ", accommodations)
print("Food: ", food)
print("Remaining Balance: ", balance)
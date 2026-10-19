# Name: Janzena Montague
# Date: October 18, 2026
# Assignment: P3LAB
# Description: This program takes a monetary amount from the user and calculates the least number of dollars and coins needed to make that amount.

# Pseudocode: 
# 1. Ask the user to enter the monetary amount in dollars and cents.
# 2. Convert the amount to cents.
# 3. Calculate the number of dollars needed.
# 4. Subtract the dollar amount from the total cents to get the remaining cents.
# 5. Calculate the number of quarters needed from the remaining cents.
# 6. Subtract the quarter amount from the remaining cents to get the new remaining cents.
# 7. Calculate the number of dimes needed from the new remaining cents.
# 8. Subtract the dime amount from the new remaining cents to get the new remaining cents.
# 9. Calculate the number of nickels needed from the new remaining cents.
# 10. Subtract the nickel amount from the new remaining cents to get the new remaining cents.
# 11. Calculate the number of pennies needed from the new remaining cents.
# 12. Display the number of dollars, quarters, dimes, nickels, and pennies needed to make the amount.
# 13. Use singular or plural forms for each denomination based on the quantity.


money = float(input("Enter the amount of money: $"))
cents = round(money * 100)
dollars = cents // 100
cents = cents - (dollars * 100)
quarters = cents // 25
cents = cents - (quarters * 25)
dimes = cents // 10
cents = cents - (dimes * 10)
nickels = cents // 5
cents = cents - (nickels * 5)
pennies = cents
if dollars > 0:
    if dollars == 1:
        print(dollars, "Dollar")
    else:
        print(dollars, "Dollars")
if quarters > 0:    
    if quarters == 1:
        print(quarters, "Quarter")
    else:
        print(quarters, "Quarters") 
if dimes > 0:
    if dimes == 1:
        print(dimes, "Dime")
    else:
        print(dimes, "Dimes")
if nickels > 0:
    if nickels == 1:
        print(nickels, "Nickel")
    else:
        print(nickels, "Nickels")
if pennies > 0:
    if pennies == 1:
        print(pennies, "Penny")
    else:
        print(pennies, "Pennies")





# Janzena Montague
# October 7, 2026
# P2HW2
# This program stores six module grades in a list and calculates the lowest grade, highest grade, sum and average of the grades.

# Pseudocode:
# Ask the user to enter a grade for each of the six modules
# Store the grades in a list
# Find the lowest grade in the list
# Find the highest grade in the list
# Calculate the sum of the grades in the list
# Calculate the average of the grades in the list
# Display the results to the user

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))
module_grades = [module1, module2, module3, module4, module5, module6]
lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_grades = sum(module_grades)
average_grade = sum_grades / 6

print()
print("------------Results------------")
print(f"{'Lowest grade:':<20}{lowest_grade}")
print(f"{'Highest grade:':<20}{highest_grade}")
print(f"{'Sum of grades:':<20}{sum_grades}")
print(f"{'Average:':<20}{average_grade:.2f}")
print("-------------------------------")

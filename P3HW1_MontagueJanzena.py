# Janzena Montague
# October 19, 2026
# P3HW1
# This program stores six module grades in a list and 
# calculates the lowest grade, highest grade, sum, average of the grades, and the letter grade for the average.


# Pseudocode:
# Ask the user to enter six module grades.
# Store the grades in a list.
# Determine the lowest grade.
# Determine the highest grade.
# Determine the sum of the grades.
# Determine the average of the grades.
# Determine the letter grade for the average.
# Display the results to the user.



mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

if avg >= 90:
   letter_grade = 'A'
elif avg >= 80:
   letter_grade = 'B'
elif avg >= 70:
    letter_grade = 'C'
elif avg >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print()
print('-------------------Grade Summary---------------')
print()
print(f'Lowest Grade: {low:.2f}')
print(f'Highest Grade: {high:.2f}')
print(f'Sum of Grades: {total:.2f}')
print(f'Average of Grades: {avg:.2f}')
print()
print('------------------Letter Grade------------------')
print()
print(f'Your Grade is: {letter_grade}')
print()
print('------------------------------------------------')




# Janzena Montague
# October 19, 2026
# P3HW2 - Employee Payroll Calculator
# This program calculates an employee's regular pay, overtime pay, and gross pay
# based on hours worked and hourly pay rate.

# Pseudocode:
# Ask the user to enter the employee's name.
# Ask the user to enter the number of hours worked.
# Ask the user to enter the hourly pay rate.
# Calculate regular pay (up to 40 hours).
# Calculate overtime pay (hours worked over 40).
# If no overtime hours, set overtime pay to 0.
# Calculate gross pay (regular pay + overtime pay).
# Display the employee's name, regular pay, overtime pay, and gross pay.

employee_name = input("Enter the employee's name: ")
hours_worked = float(input("Enter the number of hours worked: "))
hourly_pay_rate = float(input("Enter the hourly pay rate: "))

if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40
    regular_pay = regular_hours * hourly_pay_rate
    overtime_pay = overtime_hours * hourly_pay_rate * 1.5
else:
    regular_hours = hours_worked
    overtime_hours = 0
    regular_pay = regular_hours * hourly_pay_rate
    overtime_pay = 0
    
gross_pay = regular_pay + overtime_pay

overtime_display = f'${overtime_pay:.2f}'
regular_display = f'${regular_pay:.2f}'
gross_display = f'${gross_pay:.2f}'


print()
print('------------------------------------------------------------------------------------------')
print(f'Employee Name: {employee_name}')
print()
print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<18}{"RegHour Pay":<18}{"Gross Pay":<12}')
print('------------------------------------------------------------------------------------------')
print(f'{hours_worked:<15.2f}{hourly_pay_rate:<12.2f}{overtime_hours:<12.2f}{overtime_display:<18}{regular_display:<18}{gross_display:<12}')








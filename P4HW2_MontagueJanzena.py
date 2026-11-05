# Janzena Montague
# November 4, 2026
# P4HW2 - Employee Payroll Calculator
# This program calculates an employee's regular pay, overtime pay, and gross pay for multiple employees
# based on hours worked and hourly pay rate. It also displays payroll totals for all employees entered.

# Pseudocode:
# 1. Start the program
# 2. Set the total regular pay, total overtime pay, and total gross pay to 0.
# 3. Ask the user to enter the employee's name.
# 4. Use a while loop to allow the user to enter multiple employees' information until they choose to stop.
# 5. Ask the user to enter the employee's hourly pay rate.
# 6. Ask the user to enter the number of hours worked by the employee.
# 7. If the hours worked are greater than 40, calculate the regular pay for 40 hours and the overtime pay for the hours worked over 40.
# 8. Calculate overtime pay at 1.5 times the hourly pay rate for any hours worked over 40.
# 9. If no overtime hours, set overtime pay to 0 and calculate regular pay for the total hours worked.
# 10. Calculate gross pay (regular pay + overtime pay).
# 11. Increase the employee count by 1
# 12. Ask for the next employee's name
# 13. Repeat until the user enters "done" as the employee's name.
# 14. After the loop ends, display the total number of employees processed, total regular pay, 
# total overtime pay, and total gross pay for all employees entered.
# 15. End the program

total_regular_pay = 0
total_overtime_pay = 0
total_gross_pay = 0
employee_count = 0

employee_name = input("Enter the employee's name: ")
while employee_name != "Done":
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
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    employee_count += 1

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

    employee_name = input("Enter the employee's name or Done to finish): ")
    
print()
print("------------Payroll Totals------------")
print(f"{'Total Overtime Pay:':<25}${total_overtime_pay:.2f}")
print(f"{'Total Regular Pay:':<25}${total_regular_pay:.2f}")
print(f"{'Total Gross Pay:':<25}${total_gross_pay:.2f}")
print(f"{'Total Employees:':<25}{employee_count}")
print("--------------------------------------")







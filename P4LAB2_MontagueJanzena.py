# Janzena Montague
# November 4, 2026
# P4LAB2 - Multiplication Table
# Description: This program will display a multiplication table for a non-negative integer from 1 to 12 and allows 
# the user to run the program multiple times until they choose to exit.

# Pseudocode:
# 1. Start the program
# 2. Set a variable to "yes" to begin the program.
# 3. Use a while Loop to repeat while the variable is "yes".
# 4. Ask the user to enter an integer.
# 5. Check if the interger is 0 or greater.
# 6. If the integer is greater than 0, use a for Loop to count from 1 to 12.
# 7. Multiply the integer by each number and display the result.
# 8. If the integer is negative, display an error message that negative values are not allowed.
# 9. Ask the user if they would like to run the program again.
# 10. If the user enters "yes", repeat the program. 
# 11. If the user enters "no", exit the program.

run_again = "yes"
while run_again== "yes":
    number = int(input("Enter an integer: "))
    if number >= 0:
        print("Multiplication Table for", number)
        for i in range(1, 13):
            print(number, "x", i, "=", number * i)
    else:
        print("Negative values are not accepted.")
    
    run_again = input("Would you like to run the program again? (yes/no): ")

print ("Program ended.")

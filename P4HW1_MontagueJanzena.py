# Janzena Montague
# November 4, 2026
# P4HW1 - Score List
# Description: This program collects scores using Loops, checks that each score is valid,
# removes the lowest score, calculates the average, and displays a letter grade from the average.

# Pseudocode:
# 1. Start the program
# 2. Ask the user how many scores they would like to enter
# 3. Make sure the user enters at least 2 scores
# 4. Create an empty list to store the scores
# 5. Use a Loop to collect the requested number of scores from the user
# 6. Ask the user to enter a score
# 7. Check if the score is valid (between 0 and 100)
# 8. If the score is valid, add it to the list
# 9. If the score is invalid, display an error message and ask the user to enter a valid score
# 10. Repeat until all scores have been collected
# 11. Find the lowest score in the list
# 12. Remove the lowest score from the list
# 13. Calculate the average of the remaining scores
# 14. Determine the letter grade based on the average
# 15. Display the lowest score, the updated score list, the average, and the letter grade to the user.
# 16. End the program

num_scores = int(input("How many scores would you like to enter? "))
while num_scores < 2:
    print("You must enter at least 2 scores.")
    num_scores = int(input("How many scores would you like to enter? "))

score_list = []
for i in range(num_scores):
    score = float(input(f"Enter score #{i + 1}: "))
    while score < 0 or score > 100:
        print("INVALID score entered!")
        score = float(input("Enter a valid score: "))
    score_list.append(score)
lowest_score = min(score_list)
score_list.remove(lowest_score)
sum_scores = sum(score_list)
average_score = sum_scores / len(score_list)
if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"  
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print()
print("------------Results------------")
print(f"{'Lowest Score:':<20}{lowest_score}")
print(f"{'Modified List:':<20}{score_list}")
print(f"{'Scores Average:':<20}{average_score:.2f}")
print(f"{'Letter Grade:':<20}{letter_grade}")
print("-------------------------------")

      
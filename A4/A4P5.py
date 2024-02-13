# 5. Ask the user if they want to do the program.
# If they answer yes, then prompt them for two exam scores.
# Both scores must be within the range of 0 to 100.
# Display a message if the entry is outside of this range and then ask the user if they want to do this program again.
# Compute the total points to be 60% of the first score and 40% of the second score.
# Display the total points.

# main

while True:
  answer = input("Do you want to do the program? (yes/no): ")
  if answer == "yes":
    score1 = int(input("Enter the first score (0-100): "))
    score2 = int(input("Enter the second score (0-100): "))
    if score1 >= 0 and score1 <= 100 and score2 >= 0 and score2 <= 100:
      total_points = 0.6 * score1 + 0.4 * score2
      print("Total points: ", total_points)
    else:
      print("Entry is outside of the range. Please try again.")
  elif answer == "no":
    break
  else:
    print("Invalid input. Please enter 'yes' or 'no'.")
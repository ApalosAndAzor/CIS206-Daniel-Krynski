# 1. Write a loop that that accepts an integer from 10 to 20.
# If an integer outside of this range is entered tell the user the input is not accepted and give them another try. 
# Once the integer is accepted, use that number to display the integers from 0 to that number. 

# main

while True:
  number = int(input("Enter a number from 10 to 20: "))
  if number >= 10 and number <= 20:
    for i in range(1, number+1):
      print(i)
    break
  else:
    print("Input is not within 10 to 20. Please try again.")
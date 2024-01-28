#main

operation = int(input("Select which operation you would like to use: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n: "))

number_one = int(input("Input the first number: "))
number_two = int(input("Input the second number: "))

if operation == 1:
  print(f"{number_one} + {number_two} = {number_one + number_two}")
elif operation == 2:
  print(f"{number_one} - {number_two} = {number_one - number_two}")
elif operation == 3:
  print(f"{number_one} * {number_two} = {number_one * number_two}")
elif operation == 4:
  print(f"{number_one} / {number_two} = {number_one / number_two}")
else:
  print("Invalid input")
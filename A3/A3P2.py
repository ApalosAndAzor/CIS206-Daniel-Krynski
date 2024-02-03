#function

def compute(operation, number_one, number_two):
  if operation == "A":
    result = number_one + number_two
  elif operation == "S":
    result = number_one - number_two
  elif operation == "M":
    result = number_one * number_two
  elif operation == "D":
    if number_two == 0:
      result = -999
    else:
      result = number_one / number_two
  else:
    print(f"Invalid input")
  return result

#main

operation = input("Which operation you would like to use: A for Addition, S for Subtraction, M for Multiplication or D for Division: ")
number_one = int(input("Input the first number: "))
number_two = int(input("Input the second number: "))

result = compute(operation, number_one, number_two)

print(f"Number one is {number_one}")
print(f"Number two is {number_two}")
print(f"The operator code was {operation}")
if result == -999:
  print(f"You attempted to divide by zero")
else:
  print(f"The result is {result}")
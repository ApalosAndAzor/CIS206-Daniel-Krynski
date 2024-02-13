# 2.	Modify the first program to give the user 3 chances at entering proper input otherwise display a message and end the program. 

# main

count = 1

while count <= 3:
  number = int(input("Enter a number from 10 to 20: "))
  if number >= 10 and number <= 20:
    for i in range(1, number+1):
      print(i)
    break
  else:
    print("Input is not within 10 to 20.")
    count = count + 1
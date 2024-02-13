# 4. Write the code to display your list from the problem above using two different forms of a loop. 

# main

favorite_first_name = ['Alice', 'Amelia', 'Ava', 'Ethan', 'Luca', 'Mia', 'Noah', 'Oliver', 'Asher', 'Elijah']

# for loop
for name in favorite_first_name:
  print(name)

# while loop
count = 0
while count < len(favorite_first_name):
  print(favorite_first_name[count])
  count = count + 1
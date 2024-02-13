# 3.	Create a list of 10 of your favorite first names.
# Then ask the user to repeatedly enter a name and check if it is in the list.
# If the name is not in the list display a message and give the user another try. 

# main

favorite_first_name = ['Alice', 'Amelia', 'Ava', 'Ethan', 'Luca', 'Mia', 'Noah', 'Oliver', 'Asher', 'Elijah']
while True:
  check_name = input("Enter a name to check if it is in the list: ")
  if check_name in favorite_first_name:
    print("The name is in the list.")
    break
  else:
    print("The name is not in the list. Try again.")
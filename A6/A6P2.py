# 2.	Write a program that gets a string containing a person’s first, middle, and last names, and
# displays their first, middle, and last initials. For example, if the user enters John William Smith,
# the program should display J. W. S

full_name = input("Enter your first, middle and last name: ")

# Split takes each word in a string and makes it into a list
split_names = full_name.split()

# Display the initials
initials = ""
for names in split_names:
    initials += names[0].upper() + ". " # string.upper() makes the letter upper case
print("Initials: " + initials)
# name[0] takes the first letter of the name
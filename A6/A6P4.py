# 4. Vowels and Consonants
# Write a program with a function that accepts a string as an argument and returns the number of
# vowels that the string contains.
# The application should have another function that accepts a string as an argument and
# returns the number of consonants that the string contains.
# The application should let the user enter a string, and should display the number of vowels and
# the number of consonants it contains. 

def count_vowels(input_string):
    vowels = 0
    for char in input_string:
        if char.isalpha() and char.lower() in "aeiou":
            vowels += 1
    return vowels

def count_consonants(input_string):
    consonants = 0
    for char in input_string:
        if char.isalpha() and char.lower() not in "aeiou":
            consonants += 1
    return consonants

input_string = input("Type in something using the English alphabet: ")
    
vowels = count_vowels(input_string)
consonants = count_consonants(input_string)
    
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
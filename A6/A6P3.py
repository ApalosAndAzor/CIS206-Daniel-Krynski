# 3. Alphabetic Telephone Number Translator
# Many companies use telephone numbers like 555-GET-FOOD so the number is easier for their customers
# to remember.
# On a standard telephone, the alphabetic letters are mapped to numbers in the following
# fashion: A, B, and C = 2 D, E, and F = 3 G, H, and I = 4 J, K, and L = 5 M, N, and O = 6 P, Q, R,
# and S = 7 T, U, and V = 8 W, X, Y, and Z = 9.
# Write a program that asks the user to enter a 10-character telephone number in the
# format XXX-XXX-XXXX.
# The application should display the telephone number with any alphabetic characters that
# appeared in the original translated to their numeric equivalent.
# For example, if the user enters 555-GET-FOOD, the application should display 555-438-3663.

# Ask the user to enter a 10-character telephone number in the format XXX-XXX-XXXX
# creating a function that takes one parameter
input_number = input("Enter the telephone number in the format XXX-XXX-XXXX: ").upper()

phone_number = ""

for digit in input_number:
    if(digit.isalpha()):
        if (digit in "ABC"):
            phone_number += "2"
        elif (digit in "DEF"):
            phone_number += "3"
        elif (digit in "GHI"):
            phone_number += "4"
        elif (digit in "JKL"):
            phone_number += "5"
        elif (digit in "MNO"):
            phone_number += "6"
        elif (digit in "PQRS"):
            phone_number += "7"
        elif (digit in "TUV"):
            phone_number += "8"
        elif(digit in "WXYZ"):
            phone_number += "9"
    else:
        phone_number += digit

print("The phone number is", phone_number)
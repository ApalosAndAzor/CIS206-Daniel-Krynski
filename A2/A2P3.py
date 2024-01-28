#main

price = float(input("Enter the price of the book: "))
copy = int(input("Enter the number of copies: "))

option_one = 5000.00 + 20000.00
option_two = (0.125 * price) * copy
if copy > 4000:
  option_three = ((0.10 * price) * 4000) + ((0.14 * price) * (copy - 4000))
else:
  option_three = 0.10 * price * copy

print(f"Option one: {option_one}")
print(f"Option two: {option_two}")
print(f"Option three: {option_three}")

highest = max(option_one, option_two, option_three)
print(f"The highest option is: {highest}")
numbers = []

for x in range(20):
    number = float(input("Enter a number: "))
    numbers.append(number)

lowest_number = min(numbers)
highest_number = max(numbers)
total_numbers = sum(numbers)
average_number = total_numbers / 20

print(f"Lowest number: {lowest_number}")
print(f"Highest number: {highest_number}")
print(f"Total of all the numbers: {total_numbers}")
print(f"Average of all the numbers: {average_number}")
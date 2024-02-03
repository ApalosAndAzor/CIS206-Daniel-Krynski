#function

def compute(number_of_points, redemption_code):

  if redemption_code == "C":
    rewards_points = number_of_points * 2
  elif redemption_code == "X":
    rewards_points = number_of_points * 3
  else:
    rewards_points = number_of_points * 1.5

  dollar_value = rewards_points * 1.50

  return rewards_points, dollar_value

#main

number_of_points = int(input(f"How many points do you have? "))
redemption_code = input(f"What is your redemption code? (C/X/Other) ")
rewards_points, dollar_value = compute(number_of_points, redemption_code)
print(f"The amount of points is {number_of_points}")
print(f"The redemption code is {redemption_code}")
print(f"The amount of reward points is {rewards_points}")
print(f"The dollar value is ${dollar_value}")
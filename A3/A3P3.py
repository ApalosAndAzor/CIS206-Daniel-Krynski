#function

def compute(weight, zip):
  
  if weight > 100:
    weight_charge = weight * 0.02
  elif weight > 50:
    weight_charge = weight * 0.03
  else:
    weight_charge = weight * 0.05

  if zip == 60171:
    area_charge = 2.00
  elif zip == 60172:
    area_charge = 2.50
  elif zip == 60635:
    area_charge = 3.00
  else:
    area_charge = 5.00

  postage = weight_charge + area_charge
  
  return weight_charge, area_charge, postage

#main

weight = float(input("Enter the weight of the package: "))
zip = int(input("Enter the zip code: "))

weight_charge, area_charge, postage = compute(weight, zip)

print(f"The area charge is ${area_charge}")
print(f"The weight charge is ${weight_charge}")
print(f"The postage is ${postage}")
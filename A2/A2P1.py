#Main

a = int(input(f"What is the first side of the triangle? "))
b = int(input(f"What is the second side of the triangle? "))
c = int(input(f"What is the third side of the triangle? "))

if ((a*a+b*b==c*c) or (a*a+c*c==b*b) or (b*b+c*c==a*a)):
  print(f"This is a right triangle.")
else:
  print(f"This is not a right triangle.")
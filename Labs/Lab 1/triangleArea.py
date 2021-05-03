import math

def calculateArea(side1, side2, side3):
  "Calculate the area of a triangle."
  p = side1 + side2 + side3
  a = math.sqrt(p * (p - 2 * side1) * (p - 2 * side2) * (p - 2 * side3)) / 4    
  return a


area = calculateArea(20, 30, 40)
print("The area is ", area)

def bmi(p, t):
    r = p/(t**2)
    return r
   

def print_bmi_level(r):
    if r < 18.5:
        print("underweight")
    elif 18.5 <= r < 25:
        print("normal weight")
    elif 25 <= r < 30:
        print("overweight")
    elif r >= 30:
        print("obese")

    else: return bmi(p, t)

p = float(input("Enter your weight in kilograms "))
t = float(input("Enter your height in meters "))

r = bmi(p,t)
print("Your BMI is", r)
print_bmi_level(r)

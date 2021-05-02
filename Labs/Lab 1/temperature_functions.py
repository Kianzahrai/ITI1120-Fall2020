def fahrenheit_to_celsius(temp_Fahrenheit):
  "Converts temperature from Farenheit to Celsius"
  # temp_celsius is a local variable, it only exists in that function
 
  temp_Celsius = 5.0 / 9.0 * (temp_Fahrenheit - 32)
  return temp_Celsius

def celsius_to_fahrenheit(temp_Celsius):
  "Converts temperature from Celsius to Farenheit"  
  # temp_fahrenheit is a local variable, it only exists in that function
  
  temp_Fahrenheit = 9.0 / 5.0 * temp_Celsius + 32
  return temp_Fahrenheit


# t_fahrenheit and t_celsius are global variables

t_fahrenheit = 212
print(t_fahrenheit, "Fahrenheit is", fahrenheit_to_celsius(t_fahrenheit), "Celsius.")

t_celsius = 100
print(t_celsius, "Celsius is", celsius_to_fahrenheit(t_celsius), "Fahrenheit.")


t_fahrenheit = 0
print(t_fahrenheit, "Fahrenheit is", fahrenheit_to_celsius(t_fahrenheit), "Celsius.")

t_celsius = 0
print(t_celsius, "Celsius is", celsius_to_fahrenheit(t_celsius), "Fahrenheit.")

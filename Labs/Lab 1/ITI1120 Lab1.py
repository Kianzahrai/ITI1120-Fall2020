ITI1120 Lab 1
Exercise 1

x= int(input("What is the first value"))
y= int(input("What is the second value"))

intdiv = x//y
modulo = x%y

print ("The integer division is: " + str(intdiv))
print ("The remaidner is: " + str(modulo))


Exercsie 2
temp = input("Input the  temperature you like to convert? (e.g., 45C, 102C etc.) : ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")

or
def c_to_f (c):
    f = (c * (9/5)) + 32
    return (str (c) + " degrees celsius is: " str(f) + " degrees in fahrenheit")

print ("c_to_f(0)")
print (c_to_f(0))

Exercise 3
# 1. Kian's dictionary 
kian = { "name" : "Kian Zahrai", 
        "hw_average" : [85, 89, 90, 96], 
        "midterm" : [85, 86], 
        "final" : [90] 
      } 
  
# Function calculates average  
def get_average(marks): 
    total_sum = sum(marks) 
    total_sum = float(total_sum) 
    return total_sum / len(marks) 
  
# Function calculates total average 
def calculate_total_average(students): 
    hw_average = get_average(students["hw_average"]) 
    midterm = get_average(students["midterm"]) 
    final = get_average(students["final"]) 
  
    # Return the result based 
    # on weightage supplied 
    # 25 % from hw_average
    # 25 % from midterm
    # 50 % from final 
    return (0.25 * hw_average +
            0.25 * midterm + 0.5 * final) 
  
  
# Calculate letter grade of each student 
def assign_letter_grade(score): 
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else : return "E"
  
# Function to calculate the total 
# average marks of the whole class 
def class_average_is(student_list): 
    result_list = [] 
  
    for student in student_list: 
        stud_avg = calculate_total_average(student) 
        result_list.append(stud_avg) 
        return get_average(result_list) 
  
# Student list consisting the 
# dictionary of all students 
students = [kian] 
  
# Iterate through the students list 
# and calculate their respective 
# average marks and letter grade 
for i in students : 
    print(i["name"]) 
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=") 
    print("Average marks of %s is : %s " %(i["name"], 
                         calculate_total_average(i))) 
                           
    print("Letter Grade of %s is : %s" %(i["name"], 
    assign_letter_grade(calculate_total_average(i)))) 
      
    print()

Exercise 4
# If a, b and c are three sides of a triangle. Then,
# s = (a+b+c)/2
# area = sqrt(s(s-a)*(s-b)*(s-c))
# Python Program to find the area of triangle

a = 5
b = 6
c = 7

# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)

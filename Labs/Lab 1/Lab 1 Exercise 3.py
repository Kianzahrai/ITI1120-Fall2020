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

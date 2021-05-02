# Family name: Vida Dujmovic 
# Student number:  123456
# Course: IT1 1120 
# Assignment Number 1
# year 2020

import turtle 

########################
# Question 1
########################

def area_of_triangle(base, height):
     ''' (number,number)->number
     Returns the area of a triangle with a given base and height
     Precondition: base and height are non-negative numbers
     '''
     return base*height/2

#######################
# Question 2
#######################

def area_of_triangle_nice_print(base, height):
     '''(number,number)->None
      Prints a message about the area of a triangle with a given base and height
      Precondition: base and height are non-negative numbers
     '''
     print("A triangle of a base", base,"and height", height, "has area", area_of_triangle(base,height) )


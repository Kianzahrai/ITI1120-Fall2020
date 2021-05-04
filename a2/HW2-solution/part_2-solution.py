# COPYRIGHT 2020, Vida Dujmovic. All rights reserved.
# Any unauthorised distribution will constitute an infringement of copyright.
#
# Family name: Vida Dujmovic 
# Student number:  123456
# Course: IT1 1120 
# Assignment Number 2, Part 2

import math
##################################################################
# Question 1
###################################################################
def min_enclosing_rectangle(radius, x, y):
        '''(number, number, number) -> (number, number) or None

        Returns the Cartesian coordinates of the bottom left corner
        of the smallest axis-aligned rectangle that contains the circle
        of given radius and center with coordinates x,y
        
	'''
        if radius < 0:
                return None
        return x - radius, y - radius
	

###################################################################
# Question 2
###################################################################
def vote_percentage(results):
     '''(str)->number
     Precondition: results contains only words yes, no and abstain
     and result has at least one yes or no'''
     yes = results.count('yes')
     no = results.count('no')
     total = yes + no
     return yes/total

###################################################################
# Question 3
###################################################################
def vote():
     '''(None) -> None
     prints result of the vote
     '''
     votes=input("Enter the yes, no, abstain votes one by one and then press enter:\n ")
     yes_percentage = vote_percentage(votes)
     if yes_percentage == 1.00:
          print("proposal passes unanimously")
     elif yes_percentage >= 2/3:
          print("proposal passes with super majority")
     elif yes_percentage >= 1/2:
          print("proposal passes with simple majority")
     else:
          print("proposal fails")

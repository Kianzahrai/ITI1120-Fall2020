# COPYRIGHT 2020, Vida Dujmovic. All rights reserved.
# Any unauthorised distribution will constitute an infringement of copyright.
#
# Family name: Vida Dujmovic 
# Student number:  123456
# Course: IT1 1120 
# Assignment Number 3, Part 2

import math



##################################################################
# Question 1
###################################################################
def sum_odd_divisors(n):
        '''
        (int)->int

        Returns the sum of all the positive odd divisors of n unless n is zero.
        If n is zero, it returns None
        '''
        if n==0: return None
        
        dsum=0
        for i in range(1,abs(n)+1):
                if n % i == 0 and i % 2 == 1:
                        dsum=dsum+i
        return dsum


##################################################################
# Question 2
###################################################################
def series_sum():
        '''
        ()->number or None
        
        Returns the sum of series 1000 + 1/1^2 + 1/2^2 + 1/3^2 + 1/4^2 + ... + 1/n^
        for given positive integer n by the user.
        It returns None if user enters negative integer
        '''
        n=int(input("Please enter a non-negative integer: "))

        result=1000
        if n<0:
                return None
        elif n>0:
                for i in range(1,n+1):
                        result=result+1/i**2
        return result
                        
                        

##################################################################
# Question 3
###################################################################

def pell(n):
        '''(int) -> int
        Returns the n-th Pell number
        '''
        a=0
        b=1
        if n<0:
                return None
        elif n==0:
                return a
        elif n==1:
                return b
        else:
                for i in range(n-1):
                        temp=b
                        b=a + 2*b
                        a=temp
        return b


# this fails on integers bigger than 806
def pell2(n):
        return round((((1+math.sqrt(2))**n - (1-math.sqrt(2))**n))/(2*math.sqrt(2)))


# this fails on integers bigger than 1000
def pell3(n):
        '''(int) -> int
        Returns the n-th Pell number
        '''
        if n==0:
                return 0
        elif n==1:
                return 1
        else:
                return 2*pell3(n-1) + pell3(n-2)

##################################################################
# Question 4
###################################################################
def countMembers(s):
        '''(str) -> int
        Returns the number of extraordinary characters in s'''

        answer = 0
        for char in s:
                if ( (char in 'efghij') or ('F' <= char and char <= 'X')
                or ('2' <= char and char <= '6') or (char in '!,\\')):
                        answer = answer+ 1
        return answer


##################################################################
# Question 5
###################################################################
def casual_number(s):
        '''(str)->int
        Returns an integer from a casual string and None if a string does not look like integer
        Preconditions: if s is a string that look like integer then commans are in meaningful places'''
        if len(s)==0: return None

        snumber=''
        if s[0]=='-':
                snumber=snumber+s[0]
                s=s[1:]
                
        for char in s:
                if '0'<=char and char<='9':
                        snumber=snumber+char
                elif char!=',':
                        return None
        if snumber!='-':
                return int(snumber)
        else:
                return None
                        
                



##################################################################
# Question 6
###################################################################
def alienNumbers(s):
	"""
		(str) -> int
		Returns the numeric value of the alien number s
	"""

	return 1024*s.count("T")+598*s.count('y')+121*s.count('!')+42*s.count('a')+6*s.count('N') + s.count('U')
	

##################################################################
# Question 7
###################################################################
def alienNumbersAgain(s):
	"""
		(str) -> int
		Returns the numeric value of the alien number s
	"""
	
	answer = 0
	for char in s:
		if char == "T":
			answer += 1024
		elif char == 'y':
			answer += 598
		elif char == "!":
			answer += 121
		elif char == 'a':
			answer += 42
		elif char == "N":
			answer += 6
		elif char == "U":
			answer += 1
	
	return answer


##################################################################
# Question 8
###################################################################	

def encrypt(s):
	'''(str) -> str
        Returns the encrypted version of s
	'''
	
	rev = s[::-1]
	half = len(s)//2
	first_half = rev[:half]
	second_half = rev[half:] 
	second_half_rev=second_half[::-1]# second half reversed
	
	answer = ''
	for i in range(half):
		answer=answer+first_half[i]+second_half_rev[i]
	
	if len(second_half_rev) > len(first_half):
		answer=answer+second_half_rev[-1]

	return answer


##################################################################
# Question 9
###################################################################

def weaveop(s):
        '''(str)->str'''
        if len(s)<=1: return s
        result=""
        for i in range(len(s)-1):
                left=s[i]
                right=s[i+1]
                if left.isalpha() and right.isalpha():
                        result=result+left
                        if left.isupper():
                                result=result+'O'
                        else:
                                result=result+'o'

                        if right.isupper():
                                result=result+'P'
                        else:
                                result=result+'p'
                else:result=result+left
        result=result+right
        return result
                


##################################################################
# Question 10
###################################################################

def squarefree(s):
        '''str->bool'''
        for i in range(len(s)):
                for d in range(1,(len(s)-i)//2 + 1):
                        if s[i:i+d]==s[i+d:i+2*d]:
                                print(s[i:i+d], s[i+d:i+2*d])
                                return False
        return True


        
	

###################
# Question 1
###################

def atlantic(sn):
     '''(str)->str '''
     if len(sn)>=9:
          return 'nouveau'
     else:
          return 'vieux'

###################
# Question 2
###################

def southern(n):
     '''(int)->None '''
     if n==1:
          pounds = float(input("Entrez le poids en livres: "))
          ounces = float(input("Entrez le poids en onces: "))
          kilograms = (pounds * 16 + ounces) * 0.02835
          print(pounds,"livres et",  ounces, "onces est (approx.)", kilogrammes, "kilograms.")
     elif n==2:
          name = input("Quel est ton nom? ")
          studnum = input("Quel est ton numero d'etudiant? ")
          print(name, "ton numero d'etudiant est", atlantic(studnum))
          
###################
# Question 3
###################

def pacific(g1, g2, g3):
     '''(float, float, float)->bool '''
     return (g1 >= 50 and g2>=50 and g3>=50) and (g1>=80 or g2>=80 or g3>=80)

###################
# Question 4
###################

def arctic(n):
     '''(int)->bool'''
     if n // 100000 !=0: # 6 digit number
          d1 = n//100000
          d2 = (n %100000)//10000
          d3 = (n %10000)//1000
          d4 = (n %1000)//100
          d5 = (n %100)//10
          d6 = n % 10
          return d1==d6 and d2==d5 and d3==d4
     else: # 4 digit number
          d1 = n//1000
          d2 = (n %1000)//100
          d3 = (n %100)//10
          d4 = n % 10
          return d1==d4 and d2==d3
          

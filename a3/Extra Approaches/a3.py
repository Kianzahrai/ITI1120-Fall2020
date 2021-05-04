### Assignment 3 1 Part 1


print("Hello and welcome!") #greeting the user
x=1 #loop checker is initialized to True
while x>0: #loop to check if input is valid
   test=input("\nDo you want to test the number for increasing-split? Resply with a yes/no: ")
   if test.lower()!="yes": #quit program if user doesn't want to check the number
      print("Invalid input")
      exit() #quits the code
   if test.lower()=="yes": #if the user enters "yes", then continue
      try:
         n=input("Enter the number 'N': ")
         d=input("Enter the split size 'd': ")
         if int(n)<=0 or int(d)<=0: #check if the number is negative or 0
            print("Invalid input")
            continue #continue again for new input
      except: #continue again for new input
         print("Invalid input")
         continue
   x=0 #stop loop if all imput is valid

x=len(n)%int(d) # check if "d" splits "n" equally
if x!=0:
   print("The number is NOT 'strictly increasing'")
   exit() #quit if "d" doesn't split "n" into equal parts

y=int(len(n)/int(d))#calculate the number of splits and store it in "y"
if y>1:
   for z in range(0,len(n)-int(d),int(d)): #loop through all the splits
      split1=n[z:z+int(d)]
      split2=n[z+int(d):z+2*int(d)]
      if (split2<=split1): #check if split1 is <= split2
         print("The number is NOT strictly increasing")
         exit() #quit if its not increasing

for a in range(0,len(n),int(d)): #if the code reaches this part, then the number is strictly increasing
   print(n[a:a+int(d)] , end=',') # print the splits separated by ","

print ("\nThe number is 'strictly increasing'") #prints message

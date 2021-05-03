#class Time
class Time:
    #constructor calling setTime method
    # mint --> parameter for minute
    def __init__(self,hour,mint,sec):
        self.setTime(hour,mint,sec)
      
    #setTime method assigns correct value for
    #hour, minute and seconds  
    def setTime(self,hour,mint,sec):
        sec_carry=0
        min_carry=0
      
        while(sec>=60):
            sec_carry+=1
            sec=sec-60
          
        mint=mint+sec_carry
        while(mint>=60):
            min_carry+=1
            mint=mint-60
          
        hour=(hour%24)+ min_carry
      
        if(hour>=0 and hour<=23):
            self.hour=hour
            if(mint>=0 and mint<=59):
                self.minute=mint
                if(sec>=0 and sec<=59):
                    self.second=sec
                else:
                    print("Seconds cant be -ve")
                    return
            else:
                print("Minutes cant be -ve")
                return
        else:
            print("Hour cant be -ve")
            return
        print(str(self.hour)+":"+str(self.minute)+":"+str(self.second))      
      
    #function to check time 1 is before time 2        
    def isbefore(self,other):
        #matching hours
        if self.hour<other.hour:
            return True
        elif self.hour==other.hour:
            #if hours are same then check minute
            if self.minute<other.minute:
                return True
            elif self.minute==other.minute:
                #if hours and minutes same then check seconds
                if self.second<=other.second:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
      
    #function prints duration between two times      
    def duration(self,other):
        print(str(abs(self.hour-other.hour))+":"+str(abs(self.minute-other.minute))+":"+str(abs(self.second-other.second)))
          
#main method         

if __name__=="__main__":
  
    print("Initial time =",end=" ")
    #creating object for class Time
    time1=Time(12,50,34)
    print("Time set to (25,10,3)=",end=" ")
    #calling the function setTime using Time class object
    time1.setTime(25,10,63)
  
    print("Time 1: ",end=" ")
    #creating 2 Time class objects t1 & t2
    t1=Time(12,4,0)
    print("Time 2: ",end=" ")
    t2=Time(10,2,1)
  
    print("Is Time 1 before Time 2 =",end=" ")
    #chekcing t1 is before t2
    print(t1.isbefore(t2))
    print("Setting Time 2 =",end=" ")
    #chainging the value of t2
    t2.setTime(12,45,2)
    print("Is Time 1 before Time 2 =",end=" ")
    #cheking t1 is before t2
    print(t1.isbefore(t2))
  
    print("Duration = ",end=" ")
    #finding duration between t1 and t2
    t1.duration(t2)

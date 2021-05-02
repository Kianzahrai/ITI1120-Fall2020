class Time:

    def __init__(self, hh=12, mm=0, s=0):
        '''(Time)-> None'''
        self.hour = hh
        self.minute = mm
        self.second = s

        self.setTime(self.hour,self.minute,self.second)

    def setTime(self, hh=12, mm=0, s=0):
        '''(Time)-> None'''
        
        if s>59:
            self.minute+=(self.second//60)
            self.second = self.second%60
        if mm>59:
            self.hour+=(self.minute//60)
            self.minute= self.minute%60
        if hh>23:
            self.hour = self.hour%24


    #function to check time 1 is before time 2        
    def isBefore(self,other):
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
    def Duration(self,other):
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


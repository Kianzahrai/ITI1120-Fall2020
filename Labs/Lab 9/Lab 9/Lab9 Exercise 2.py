class Car:
    #Method to initialize class
    def __init__(self, brand='Ford', color='Red'):
        self.brand = brand
        self.color = color
        self.pilote = 'Person'
        self.speed = 0

    def __repr__(self):
        return "{} {} driven by {}, speed = {} m/s.".format(self.color,self.brand,self.pilote,self.speed)

    def __eq__(self, other):
        #Override the defauls Equality function behavior
        return self.color == other.color and self.brand == other.brand and self.pilote == other.pilote and self.speed == other.speed

    
    #Method to change driver
    def choice_driver(self, driver):
        if driver:
            self.pilote = driver

    #Method to accelerate car
    def accelerate(self,flow=0,duration=0):
        if flow != 0 and duration != 0 and self.pilote == 'Person':
            print("This car does not have a driver!")
        else:
            self.speed += flow*duration
    #Method to display all info
    def display_all(self):
        print(self.color,self.brand,' driven by ',self.pilote+', speed = ',self.speed, ' m/s.')



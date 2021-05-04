class Person(object): # A person has a last name and first name
    def __init__(self, lastName, firstName):
        self.lastName = lastName
        self.firstName = firstName
    

    def __repr__(self):
        return "Last name: "+ self.lastName + "; First name: " + self.firstName

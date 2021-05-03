#Experimenting with derived classes and inheritance
class BankAccount:
    def __init__(self,name = 'Dupont', sold = 1000):
        self.name = name
        self.sold = sold

    def deposit(self,sums=0):
        self.sold += sums

    def withdraw(self,sums=0):
        self.sold -= sums

    def display(self):
        print("The sold of the Bank account of ",self.name," is ",self.sold," dollars.")

class AccountSaving(BankAccount):
    def __init__(self, name='Dupont',solde = 1000):
        BankAccount.__init__(self,name = 'Dupont', sold = 1000)
        self.rate= 0.003
        self.name = name
        self.sold = sold

    def changeRate(self, value = 0.003):
            self.rate = value

    def Capitalisation(self, Month):
        print("Capitalisation of ", Month," at the monthly rate of ",self.rate*100," %.")
        for i in range(Month-1):
            self.sold = self.solde*(1+self.rate)

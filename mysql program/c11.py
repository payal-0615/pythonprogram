class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited =", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawn =", amount)
        else:
            print("Insufficient Balance")

    def showbalance(self):
        print("Name =", self.name)
        print("Bank Balance =", self.balance)


# object creation
b1 = Bank("Payal", 10000)

b1.showbalance()
b1.deposit(5000)
b1.showbalance()
b1.withdraw(3000)
b1.showbalance()
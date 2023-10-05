
class Account:
    def __init__(self, id, owner, balance):
        self.id = id
        self.owner = owner
        self.balance = balance

    def display(self):
        print(self.id, self.owner, self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("invalid amount", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("not enough balance")


a1 = Account(1001, "Paul Smith", 1200)
a2 = Account(1002, "John Doe", 3900)

a1.deposit(100)
a2.withdraw(200)

a1.display()
a2.display()




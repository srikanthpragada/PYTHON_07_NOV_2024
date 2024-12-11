class BalanceError(Exception):
    def __init__(self):
        self.message = "Insufficient Balance"

    def __str__(self):
        return self.message


class SavingsAccount:
    minbal = 10000

    @staticmethod
    def getminbal():
        return SavingsAccount.minbal

    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            #raise ValueError('Insufficient Balance')
            raise BalanceError()

        self.balance -= amount


    def getBalance(self):
        return self.balance

    @property
    def currentbalance(self):
        return self.balance


a1 = SavingsAccount(1, "Scott", 100000)
a2 = SavingsAccount(2, "Jack")

a1.deposit(10000)
a1.withdraw(200000)
print(a1.getBalance())
print(a1.currentbalance)  # property

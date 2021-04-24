for i in "imran":
    print(i)


class ATM:
    def __init__(self, money):
        self.money = money

    def withdraw(self, amount):
        self.money -= amount
        print(f"You withdraw {amount}")

    def deposit(self, amount):
        self.money += amount
        print(f"You deposit {amount}")

    def get_deposit(self):
        print("your balance", self.money)


atm = ATM(money = 0)

atm.withdraw(30)
atm.deposit(40)

atm.get_deposit()

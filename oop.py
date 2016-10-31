#Creating parent class from which a subclass Saving
#sets a minimum account balance to 1000 beyond which a sure cannot withdraw
# defines methods to deposit and withdraw from the account
class Account():
    def deposit():
        pass
    # Creating class Savings, setting initial balance at 1000


class Savings(Account):
    def __init__(self):
        self.balance = 1000

    def deposit(self, deposit):
        if type(deposit) == int and deposit != "":
            if deposit >= 0:
                self.balance += deposit
                return self.balance
            else:
                return "Invalid deposit amount"
        else:
            raise ValueError()

    def withdraw(self, amount):
        if type(amount) == int and amount != "":
            if amount > 0:
                if (self.balance - amount) > 0:
                    if (self.balance - amount) > 1000:
                        self.balance -= amount
                        return self.balance
                    else:
                        return "Can't withdraw more than threshold balance"
                else:
                    return "Can't withdraw beyond Account balance"
            else:
                return "Invalid amount"
        else:
            raise ValueError()
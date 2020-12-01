class User ():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def make_withdraw(self, amount):
        self.balance = self.balance - amount
        return self

    def display_user_balance(self):
        return (f"{self.name}'s' balance is now ${self.balance}")
    # if i dont return anything it gives a default value of None. if I return "Self" it retruns the location of where this user object is stored.

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance = other_user.balance + amount
        return self


'''BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance'''

michael = User("michael", 5000)
sadie = User("sadie", 0)

michael.transfer_money(sadie, 4999)
print(sadie.balance)
print(michael.balance)

''' creating 3 instances of the user class object'''

print(michael.make_deposit(9).make_withdraw(10).make_deposit(
    100).transfer_money(sadie, 100).display_user_balance())

print(michael.display_user_balance())

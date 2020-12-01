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
        print((f"{self.name}'s' balance is now ${self.balance}"))
        return self

    def transfer_money(self, other_user, amount):
        if self.balance < amount:
            print("Insufficient Funds!")
        self.balance = self.balance - amount
        ID_2.make_deposit(amount)
        return self
        # figure out a way to make this dynamic instead of hard coding where the money is being transfered to


ID_1 = User("Michael", 500)
ID_2 = User("Sadie", 0)
ID_3 = User("John", 1000)
''' creating 3 instances of the user class object'''

ID_2.make_deposit(100).make_deposit(200).make_deposit(
    300).make_withdraw(50).display_user_balance()
# chaining methods. in order for this to work, the methods must return self at the end.
# This is called chaining. In order for this to work, each method must return self.
# By returning self, if we recall how functions work, each method call will now be equal to the instance that called it.


# print(ID_1.name)
# print(ID_1.balance)

# ID_1.make_deposit(50000)

# # ID_1.make_withdraw(300)
# print(ID_1.balance)

# message = ID_1.display_user_balance()
# print(message)


# ID_2.transfer_money(ID_1, 500)
# print(ID_1.display_user_balance())
# ID_1.transfer_money(ID_2, 500)
# print(ID_1.display_user_balance())
# print(ID_2.display_user_balance())

# random = input("here:")
# print(random)

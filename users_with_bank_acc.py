class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, this is where we specify the attributes for our class)
        # don't worry about user info here; we'll involve the User class soon]

    def __str__(self):
        return (f"Here is the the starting interest rate of {self.int_rate} and balance of {self.balance}")

    def deposit(self, amount):
        # your code here
        self.balance = self.balance + amount
        print(f"You have deposited {amount}")
        return self

    def withdraw(self, amount):
            # your code here
        self.balance = self.balance - amount
        print(f"You have withdrew {amount}")
        return self

    def display_account_infocopy(self):
            # your code here
        print(f"Your balance is {self.balance}")
        return self

    def yield_interest(self):
        self.balance = (self.balance * self.int_rate) + self.balance
        print(f"Your new balance after interest is: {self.balance}")
        return self
        # your code here


# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.account = BankAccount(int_rate=0.02, balance=0)  # added this line


# class User:
#     def example_method(self):
#         # we can call the BankAccount instance's methods
#         self.account.deposit(100)
#         print(self.account.balance)		# or access its attributes
class User ():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.025, 0)

    def __str__(self):
        return (f"{self.name}, {self.email}, {self.account}")

    def make_deposit(self, amount):
        self.account.deposit(amount)
        # self.account.balance += amount
        print("Your balance is", self.account.balance)
        return self
        # self.account.deposit(100)
        # print(self.account.balance)
        # self.balance = self.balance + amount

    def make_withdraw(self, amount):
        # self.balance = self.balance - amount
        self.account.withdraw(amount)
        # self.account.balance -= amount
        print("You have withdrawn", amount)
        return self

    def display_user_balance(self):
        print(f"{self.name}'s' balance is now ${self.account.balance}")
        return self
    # <bound method User.display_user_balance of <__main__.User object at 0x00000211B5535FD0>>

    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance = other_user.account.balance + amount
        return self


john = User("john", "john@john@gmail.com")
sadie = User("Sadie", "sadie@sadie.com")
print(john)
john.make_deposit(500).make_withdraw(
    1000).make_deposit(10).display_user_balance()

john.transfer_money(sadie, 500)
print(sadie.account.balance)
print(john.account.balance)
# attributes and methods are available from our Bank Account class because it was set as an attribute in our constructor __init__magic method

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
        if self.balance < amount:
            print("not enough dollars!!")
        self.balance = self.balance - amount
        print(f"You have withdrew {amount}")
        return self

    def display_account_infocopy(self):
            # your code here
        print(f"Your balance is {self.balance}")
        return self

    def yield_interest(self):
        if self.balance <= 0:
            print("no more money!")
        self.balance = (self.balance * self.int_rate) + self.balance
        print(f"Your new balance after interest is: {self.balance}")
        return self
        # your code here


new_bank_account = BankAccount(0.025, 1000)
# print(new_bank_account)

# new_bank_account_2 = BankAccount(0.030, 500)
# print(new_bank_account_2)
# new_bank_account_2.deposit(500).deposit(500).withdraw(
#     1000).yield_interest().display_account_infocopy()


print(new_bank_account.balance)
new_bank_account.deposit(500).deposit(500).withdraw(
    3000).yield_interest().display_account_infocopy()

class BankAccount:
    def __init__(self, int_rate, balance):
        self.rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance: " + str(self.balance))
        return self

    def yield_interest(self):
        self.balance = self.balance + self.balance * self.rate
        return self

class User:
    def __init__(self, name, email, rate):
        self.name = name
        self.email = email
        self.account_balance = 0
        self.account = BankAccount(rate, self.account_balance)
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account.deposit(amount)


    def make_withdrawal(self, amount):
        self.account.withdraw(amount)


    def display_user_balance(self): #"User: Guido van Rossum, Balance: $150
        self.account.display_account_info()

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.make_deposit(amount)
        return self
a = User("a", 0, 0.01)
a.display_user_balance()

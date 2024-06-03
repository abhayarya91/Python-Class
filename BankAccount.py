class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def withdrawal(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def bankFees(self):
        fees = 0.05 * self.balance
        self.balance -= fees
        print("Bank fees applied.")

    def display(self):
        print("Account Number:", self.accountNumber)
        print("Account Holder Name:", self.name)
        print("Account Balance:", self.balance)
    
    def transfer(self, amount, recipient):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient.deposit(amount)
            print("Transfer successful.")
        else:
            print("Invalid transfer amount or insufficient balance.")

    def apply_interest(self, rate):
        interest = (rate / 100) * self.balance
        self.balance += interest
        print("Interest applied.")

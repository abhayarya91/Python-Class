class BankAccount:
    bank_fee_rate = 0.05
    
    def __init__(self, account_number, name, balance, mobile_number):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.mobile_number = mobile_number
    
    def deposit(self, amount):
        self.balance += amount
        self._apply_bank_fee()
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self._apply_bank_fee()
        else:
            print("Insufficient funds")
    
    def transfer(self, recipient, amount):
        if amount <= self.balance:
            self.balance -= amount
            recipient.deposit(amount)
            self._apply_bank_fee()
        else:
            print("Insufficient funds")
    
    def display_balance(self):
        print(f"Account Balance for {self.name}: {self.balance}")
    
    def _apply_bank_fee(self):
        fee = self.balance * self.bank_fee_rate
        self.balance -= fee
    
    def calculate_interest(self, interest_rate):
        interest = self.balance * interest_rate
        self.balance += interest
        print(f"Interest added: {interest}")
        
    # Method to get account details
    def get_details(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance}, Mobile Number: {self.mobile_number}"

if __name__ == "__main__":
    print("Welcome to the Bank System!")
    
    # Creating accounts
    account1 = BankAccount("1234", input("Enter name for Account 1: "), float(input("Enter balance for Account 1: ")), input("Enter mobile number for Account 1: "))
    account2 = BankAccount("5678", input("Enter name for Account 2: "), float(input("Enter balance for Account 2: ")), input("Enter mobile number for Account 2: "))
    
    print("\nCommands:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer funds")
    print("4. Display balance")
    print("5. Calculate interest")
    print("6. Display account details")
    print("7. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-7): ")
        if choice == "1":
            amount = float(input("Enter the amount to deposit: "))
            account_num = input("Enter account number: ")
            if account_num == account1.account_number:
                account1.deposit(amount)
            elif account_num == account2.account_number:
                account2.deposit(amount)
            else:
                print("Invalid account number")
        
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: "))
            account_num = input("Enter account number: ")
            if account_num == account1.account_number:
                account1.withdraw(amount)
            elif account_num == account2.account_number:
                account2.withdraw(amount)
            else:
                print("Invalid account number")
        
        elif choice == "3":
            amount = float(input("Enter the amount to transfer: "))
            sender_account_num = input("Enter sender's account number: ")
            recipient_account_num = input("Enter recipient's account number: ")
            if sender_account_num == account1.account_number and recipient_account_num == account2.account_number:
                account1.transfer(account2, amount)
            elif sender_account_num == account2.account_number and recipient_account_num == account1.account_number:
                account2.transfer(account1, amount)
            else:
                print("Invalid account numbers")
        
        elif choice == "4":
            account_num = input("Enter account number to display balance: ")
            if account_num == account1.account_number:
                account1.display_balance()
            elif account_num == account2.account_number:
                account2.display_balance()
            else:
                print("Invalid account number")
        
        elif choice == "5":
            account_num = input("Enter account number to calculate interest: ")
            interest_rate = float(input("Enter interest rate (e.g., 0.02 for 2%): "))
            if account_num == account1.account_number:
                account1.calculate_interest(interest_rate)
            elif account_num == account2.account_number:
                account2.calculate_interest(interest_rate)
            else:
                print("Invalid account number")
        
        elif choice == "6":
            account_num = input("Enter account number to display details: ")
            if account_num == account1.account_number:
                print(account1.get_details())
            elif account_num == account2.account_number:
                print(account2.get_details())
            else:
                print("Invalid account number")
        
        elif choice == "7":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


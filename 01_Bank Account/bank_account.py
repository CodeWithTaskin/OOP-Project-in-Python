class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposit(self):
        amount = int(input(f"Please enter your deposit amount: $"))
        self.balance += amount
        print("Your deposit is successful!")
    def widrow(self):
        amount = int(input(f"Please enter your widrow amount: $"))
        if self.balance < amount:
            print(f"Sorry you have ${self.balance}.You can't widrow ${amount}.")
        else:
            self.balance -= amount
            print(f"You successfully widrow ${amount}.")
    def display(self):
        print(f"Your balance is ${self.balance}")
        

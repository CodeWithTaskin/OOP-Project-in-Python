from bank_account import BankAccount
account = BankAccount()

while True:
    user_choice = input("What do you want?(Deposit/Widrow/Display or quit): ")
    if user_choice.lower() == "deposit":
        account.deposit()
    elif user_choice.lower() == "widrow":
        account.widrow()
    elif user_choice.lower() == "display":
        account.display()
    elif user_choice.lower() == "quit":
        print("Good Bye👋👋👋")
        break

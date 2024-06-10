from replit import clear
from calculater import Calculator
cal = Calculator()
while True:
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    userChoice = int(input("""
________________MENU_________________
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Reminder
Anything else to exit.: """))

    clear()
    if userChoice == 1:
        print(f"Result is :{cal.addition(x,y)}")
    elif userChoice == 2:
        print(f"Result is :{cal.subtraction(x,y)}")
    elif userChoice == 3:
        print(f"Result is :{cal.multiplication(x,y)}")
    elif userChoice == 4:
        print(f"Result is :{cal.division(x,y)}")
    elif userChoice == 5:
        print(f"Result is :{cal.reminder(x,y)}")
    else:
        break
    
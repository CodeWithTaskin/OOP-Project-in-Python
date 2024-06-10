from number_guessing_game import Guess,Mode

mode = Mode()
guess = Guess()
ranGuess = guess.random_guess()
userMode = input("What level you want to play?(easy/hard): ")
try:
    life = mode.get_life(userMode)
except ValueError as e:
    print(e)
    exit()

while True:
    print(ranGuess)
    print(f"You have {life} life")

    try:
        userGuess = int(input("Guess a number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if ranGuess > userGuess:
        life -= 1
        print("Too low...")
    elif ranGuess < userGuess:
        life -= 1
        print("Too high...")
    else:
        print("Your guess is currect")
        break

    if life == 0:
        break
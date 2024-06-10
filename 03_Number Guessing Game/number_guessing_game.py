import random as r

class Guess:
    def __init__(self):
        self.__value = 0
    
    def random_guess(self):
        random_guess = r.randint(1,100)
        return random_guess

class Mode:
    def __init__(self):
        self.__easy = 0
        self.__hard = 0


    def get_life(self,mode):
        if mode == "easy":
            self.__easy = 10
            return self.__easy
        elif mode == "hard":
            self.__hard = 5
            return self.__hard
        else:
            raise ValueError("Invalid mode. Choose 'easy' or 'hard'.")
    
        
        
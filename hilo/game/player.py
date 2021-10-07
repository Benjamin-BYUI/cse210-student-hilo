import random

class Player:
    def __init__(self):
        self.current_card = random.randint(1, 13)
    
    def get_points(self, player_guess):
        next_card = random.randint(1, 13)
        return_score = 0
        if self.current_card > next_card and player_guess == "l":
            return_score = 100
        elif self.current_card < next_card and player_guess == "h":
            return_score = 100
        elif self.current_card == next_card:
            return_score = 0
        else:
            return_score = -75
        self.current_card = next_card
        return return_score, next_card
    
    def get_guess(self):
        guess = input ("Higher or lower? [h/l] ")
        return guess

import random

class Player:
    def __init__(self):
        self.current_card = random.randint(1, 13)
        self.next_card = None # todo
    def get_points(self, player_guess):
        if self.current_card < self.next_card and player_guess == "l":
            return 100
        elif self.current_card > self.next_card and player_guess == "h":
            return 100
        else:
            return 75

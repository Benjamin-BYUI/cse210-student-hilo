import random

class Player:
    def __init__(self):
        self.current_card = random.randint(1, 13)
        self.next_card = None # todo

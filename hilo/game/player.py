import random

class Player:
    """Keeps track of the last card displayed. Calculates score change and
    draws next card. Gets player input.

    Attributes:
        current_card (int): The last card displayed.
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Player): an instance of Player.
        """
        self.current_card = random.randint(1, 13)

    def get_points(self, player_guess):
        """Calculates the change in points and draws and returns next card.

        Args:
            self (Player): an instance of Player.
            player_guess (str): guess from player.
        """
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
        """Get a guess of high (h) or low (l) from the player

        Args:
            self (Player): an instance of Player.
        """
        guess = input ("Higher or lower? [h/l] ")
        return guess

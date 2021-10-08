from game.player import Player

class Dealer:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        player (Player): An instance of the class of objects known as Player.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.keep_playing = True
        self.score = 300
        self.player = Player()
        self.last_guess = None
        self.next_card = None

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        while self.keep_playing:
            print(f"The card is: {self.player.current_card}")
            self.get_guess()
            self.do_score_update()
            self.do_outputs()
        print("Thanks for playing!")

    def get_guess(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means the player's guess.

        Args:
            self (Dealer): An instance of Dealer.
        """
        self.last_guess = self.player.get_guess()
        
    def do_score_update(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Dealer): An instance of Dealer.
        """
        points, self.next_card = self.player.get_points(self.last_guess)
        self.score += points
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the card that was dealt and the score.

        Args:
            self (Dealer): An instance of Dealer.
        """
        print(f"Next card was: {self.next_card}")
        print(f"Your score is: {self.score}")
        if self.score > 0:
            choice = input("Keep playing? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            print("Game over!")
            self.keep_playing = False
        print()
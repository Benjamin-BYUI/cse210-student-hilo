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

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means throwing the dice.

        Args:
            self (Dealer): An instance of Dealer.
        """
        self.player.throw_dice()
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Dealer): An instance of Dealer.
        """
        points = self.player.get_points()
        self.score += points
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the dice that were rolled and the score.

        Args:
            self (Dealer): An instance of Dealer.
        """
        print(f"\nYou rolled: {self.player.dice}")
        print(f"Your score is: {self.score}")
        if self.player.can_throw():
            choice = input("Roll again? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False
from Displays import LCDDisplay
from Button import *
from Buzzer import *

class DinoGame:
    """ my implementation of the Running Man Game
        2 buttons for starting the game and making character jump
        Buzzer to make sounds
        LCD display to show animation
    """
    
    class Game:
    def __init__(self):
        self.player = Player()
        self.obstacles = []
        self.score = Score()
        self.running = True

def main():
    # Initialize display, animation, player, obstacle, score, etc.
    display = Display()
    animation = animation(display)
    player = Player(animation)
    obstacle = Obstacle(animation)
    score = Score()
    game = Game(animation)
    input_handler = Input(player)

    while True:
        # Check input
        if jump_button_pin.value():
            input_handler.handle_input()  # Handle jump action

        # Update game state
        player.update()
        obstacle.update()
        score.increase()  # Update score

    # Run the main function
if __name__ == "__main__":
    main()

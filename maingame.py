import time
from Displays import LCDDisplay
from Button import *
from Character import Character
from Obstacle import Obstacle
from Game import Game

def main():
    # Initialize the game
    game = Game()
    game.start()

if __name__ == "__main__":
    main()

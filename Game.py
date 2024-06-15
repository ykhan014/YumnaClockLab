import time
import random
from Displays import LCDDisplay
from Button import Button
from Character import Character  
from Obstacle import Obstacle

class Game:
    def __init__(self):
        self._display = LCDDisplay(sda=0, scl=1, i2cid=0)
        self.button_jump = Button(13, 'jump', buttonhandler=self)
        self.button_startresume = Button(12, 'start', buttonhandler=self)  
        self.character = Character(row=1, col=0, display=self._display) 
        self.obstacles = []
        self.is_game_over = False
        self.jump_pressed = False
        self.startresume_pressed = False  # Initialize start/resume button state

    def buttonPressed(self, name):
        if not self.is_game_over:
            if name == 'jump':
                self.character.perform_jump()
            elif name == 'start':
                self.startresume_pressed = True  # Handle start/resume button press

    def start(self):
        self._display.showText("  Let the Game   Begin", row=0, col=0)
        time.sleep(3)
        self._display.clear()

    def update(self):
        self.character.update_position()
        for obstacle in self.obstacles:
            obstacle.move()
            if self.check_collision(self.character, obstacle):
                self.game_over()
        
        # Randomly add obstacles
        if random.randint(1, 10) > 8:
            new_obstacle = Obstacle(a=16, b=1, type='spike', display=self._display)
            self.obstacles.append(new_obstacle)

    def check_collision(self, character, obstacle):
        return character.row == obstacle.aposition and character.col == obstacle.bposition

    def game_over(self):
        self.is_game_over = True

    def game_over_screen(self):
        self._display.clear()
        self._display.showText("  Game Over", row=0, col=0)
        time.sleep(5)
        self.reset_game()

    #Reset all game state

    def reset_game(self):
        self.__init__()  

    def display_game(self):
        self.character.render()
        for obstacle in self.obstacles:
            obstacle.draw()

if __name__ == "__main__":
    game = Game()
    game.start()
    while not game.is_game_over:
        game.update()
        game.display_game()
        time.sleep(0.1) 
    game.game_over_screen()


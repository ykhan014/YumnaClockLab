from Displays import LCDDisplay
import time

# Main character class controlled by the player.
class Character:
    # Character's heart shape definition
    character_shape = [0x00, 0x00, 0x1B, 0x1F, 0x0E, 0x04, 0x00, 0x00]

    def __init__(self, row, col, display):
        self.row = row
        self.col = col
        self.display = display
        self.display.addShape(0, Character.Character_shape)
        self.state = "running"
        self.jump_height = 0
        self.is_visible = False

    def perform_jump(self):
        print("Character jumps")
        self.state = "jumping"
        self.jump_height = 2

    def start_running(self):
        print("Character runs")
        self.state = "running"
        self.row = 1

    def update_position(self):
        if self.state == "jumping" and self.jump_height > 0:
            self.col -= 1
            self.jump_height -= 1
        else:
            self.col = 1

    def render(self):
        self.display.clear()
        self.display.showText(f"{chr(0)}", self.col, self.row)

    def show_character(self):
        self.is_visible = True
        self.render()

    def detect_collision(self, obstacle):
        return self.row == obstacle.row and self.col == obstacle.col


from Displays import LCDDisplay

# Obstacle class
class Obstacle:
    # Obstacle's spike shape definition
    spike_shape = [0x00, 0x00, 0x00, 0x00, 0x04, 0x04, 0x0E, 0x1F]  

    def __init__(self, a, b, type, display):
        self.aposition = a
        self.bposition = b
        self.type = type
        self.display = display
        if self.type == 'spike':
            self.display.addShape(1, Obstacle.spike_shape) 

    def move(self):
        self.aposition -= 1

    def draw(self):
        if self.type == 'spike':
            self.display.showText(f"{chr(1)}", self.bposition, self.aposition)  # Display custom character at position 1

# Additional Usage
if __name__ == "__main__":
    # Initialize the display
    display = LCDDisplay(sda=0, scl=1, i2cid=0)

    # Creating an obstacle of type 'spike'
    obstacle = Obstacle(a=15, b=0, type='spike', display=display)

    # Drawing the obstacle on the display
    obstacle.draw()

    # Move the obstacle and redraw
    for _ in range(5):
        obstacle.move()
        display.clear()  
        obstacle.draw()
        time.sleep(1)  

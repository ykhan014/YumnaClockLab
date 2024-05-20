from Displays import LCDDisplay
from Button import *
from Clock import *

class ClockController:
    """ Our implementation of the CLOCK cONTROLLER
        4 buttons for setting month, date, hour, min
        LCD display to show the time
    """
    
    def __init__(self):
        self._clock =  Clock()
        self._display = LCDDisplay(sda=0, scl=1, i2cid=0)
        self._buttons = [Button(10, 'white', buttonhandler=self),
                         Button(10, 'red', buttonhandler=self),
                         Button(10, 'yellow', buttonhandler=self),
                         Button(10, 'blue', buttonhandler=self)]
    def showTime(self):
        """ Show the time on the display """

        (year, month, date, hour, minute, sec, wd, yd) = self._clock.getTime()    
        self._display.showText(f'{month:02d}/{date:02d} {hour:02d}:{minute:02d}:{sec:02d}')  

    def buttonPressed(self,name):
        pass


    def buttonReleased(self, name):
        pass                       

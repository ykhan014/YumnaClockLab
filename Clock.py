from Counters import Time

class Clock:
    """
    Our implementation of the Clock class
    """

    def getTime(self):
        return Time.getTime()

    def setTime(self, timetuple):
        Time.setTime(timetuple)

    def getHour(self):        
        """ return the current hour as an int """

        timetuple = Time.getTime()
        return timetuple[3]

    def setHour(self, hour):
        """ Sets the RTC hHour o the hour parameter """
        # First get the current time from system
        timetuple = Time.getTime()
        # Convert the tuple into a list    
        timelist = list(timetuple)
        # Change the hour to the new hour
        timelist[3] = hour
        # save it back to the system
        Time.setTime(timelist)

    def getMinute(self):
        pass

    def setMinute(self,minute):
       pass

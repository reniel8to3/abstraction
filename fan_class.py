#create class fan
class fan:
    #set default values
    def __init__(self,speed = 'SLOW', radius = 5, power = 0, color ='blue'):
    #private variables
        self.__speed = speed
        self.__radius = radius
        self.__power = power
        self.__color = color
    #get values
    def fan_speed_setter (self):
        if self.__speed == 1:
            self.__speed = 'slow'
        elif self.__speed == 2:
            self.__speed = 'medium'
        elif self.__speed == 3:
            self.__speed = 'fast'
    def radius_setter (self):
        return self.__radius
    def color_setter (self):
        return self.__color
    def power_setter (self):
        if self.__power == 0:
            self.__power = 'off'
        elif self.__power == 1:
            self.__power = 'on'

    def fan_speed_getter (self):
        return str(self.__speed)
    def radius_getter (self):
        return self.__radius
    def color_getter (self):
        return self.__color
    def power_getter (self):
        return str(self.__power)
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
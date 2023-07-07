#create class
class car:
#add attributes
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    #add methods for acceleration and brake (na kami eme)
    def acceleration(self):
        self.__speed += 5
    def brakenakamieme(self):
        self.__speed -= 5
    #return values
    def valuereturn(Self):
        return self.__speed
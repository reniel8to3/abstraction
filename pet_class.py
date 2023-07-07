#create class
class pet:
#create constructors
    def __init__(self):
        self.__name =""
        self.__animal_type=""
        self.__age=0
#ask for pet name
    def set_name(self):
        self.__name=str(input("Your pet's name is: "))
#ask for animal type
    def set_animal_type(self):
        self.__animal_type=str(input("Your pet is a/an: "))
#ask for pet age
    def set_age(self):
        self.__age=str(input("Your pet's age is: "))
#return name, type and age
    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__animal_type
    def get_age(self):
        return self.__age
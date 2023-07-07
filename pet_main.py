#import pet
from pet_class import pet
import pyfiglet
import time
#create pet
pet_meowarf=pet()
#input all pet data needed
pet_meowarf.set_name()
pet_meowarf.set_animal_type()
pet_meowarf.set_age()
#return all pet data
meow = pyfiglet.figlet_format("processing", font = "linux" )
print(meow)
print("Your pet's name is: ", pet_meowarf.get_name())
time.sleep(0.5)
print("Your pet is a/an: ",pet_meowarf.get_animal_type())
time.sleep(0.5)
print("Your pet's age is ", pet_meowarf.get_age())
#import car
from car_class import car
import pyfiglet
import time
#create car vroom vroom
vroomvroom = car(None,None)
#accelerate for five times vroom vroom vroommmm
result = pyfiglet.figlet_format("Let's ride...", font = "bubble" )
print(result)
for i in range(5):
    vroomvroom.acceleration()
    print("\nThe car's current speed is:", vroomvroom.valuereturnspeed())
    time.sleep(0.5)
#hit the brakes five times stopppp
result = pyfiglet.figlet_format("Let's slow it down...", font = "bubble")
print (result)
for i in range(5):
    vroomvroom.brakenakamieme()
    print("\nThe car's current speed is:", vroomvroom.valuereturnspeed())
    time.sleep(0.5)

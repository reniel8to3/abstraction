#import class
from fan_class import fan
import pyfiglet 
#create 2 objects
fan_1 = fan(3, 10, 'yellow', True)
fan_2 = fan(1, 5, 'blue', False)
#set and return values
fan_1.fan_speed_setter()
fan_1.radius_setter()
fan_1.color_setter()
fan_1.power_setter()
print('The speed of Fan 1 is ' ,fan_1.fan_speed_getter(), ' and its radius is ' ,fan_1.radius_getter(), ' while the fan is ' ,fan_1.color_getter(), ' and its color is ' ,fan_1.power_getter(), '.')

fan_2.fan_speed_setter()
fan_2.radius_setter()
fan_2.color_setter()
fan_2.power_setter()
print('The speed of Fan 2 is ' ,fan_2.fan_speed_getter(), ' and its radius is ' ,fan_2.radius_getter(), ' while the fan is ' ,fan_2.color_getter(), ' and its color is ' ,fan_2.power_getter(), '.')
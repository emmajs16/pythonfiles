from temp_conversions import *


print("{:11s}\t\t{:<10s}\t|\t{:<10s}\t\t{:<10s}".format("Celsius","Fahrenheit","Fahrenheit","Celsius"))
celsius = 40
fahrenheit = 120
while True:
    print("{:.1f}\t\t{:<10.1f}\t|\t{:<10.1f}\t\t{:<10.2f}".format(celsius,celsius_to_fahrenheit(celsius),fahrenheit,fahrenheit_to_celsius(fahrenheit)))
    celsius -=1
    fahrenheit-=10
    if fahrenheit < 30:
        break

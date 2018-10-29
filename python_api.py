import json
import urllib2
from urllib import urlopen



city = str(input("Please enter your city: "))
state = str(input("Please enter your state: "))
coat = False
umbrella = False

url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{}%2C%20{}%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys".format(city,state)

result = dict(json.load(urllib2.urlopen(url)))

temperature = int(result.get('query').get('results').get('channel').get('item').get('condition').get('temp'))
condition = result.get('query').get('results').get('channel').get('item').get('condition').get('text')

if temperature <= 45:
    coat = True
if condition == "rainy":
    umbrella = True
print("\nTemperture: {} degrees".format(temperature))
print("It is {} outside.\n".format(condition.lower()))
if coat == True:
    print("You might want to wear a coat today!")
if umbrella == True:
    print("You might want to bring an umbrella today!")

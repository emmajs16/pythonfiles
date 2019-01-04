import json
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

coat = False
umbrella = False

# loop this until the user says they don't want to search another city
while True:
    # User enters their city and state
    city = str(input("Enter your city: ")).replace(" ", "")
    state = str(input("Enter your state: "))
    # Get's data from yahoo weather api using JSON
    # Concatenates the user's location into the url string
    url = urlopen("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{}%2C%20{}%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys".format(city,state))
    result = dict(json.load(url))
    # Uses the data to set the current temperature and condition variables
    temperature = int(result.get('query').get('results').get('channel').get('item').get('condition').get('temp'))
    condition = result.get('query').get('results').get('channel').get('item').get('condition').get('text')


    print("\nTemperture: {} degrees".format(temperature))
    print("It is {} outside.\n".format(condition.lower()))
    # if the temp is less than 45 wear a coat
    if temperature <= 45:
        print("You might want to wear a coat today!")
    # if it's raining outside bring an umbrella
    if condition == "rain":
        print("You might want to bring an umbrella today!")
    # ask the user if they would like to enter another city, if they don't break loop
    newCity = str(input("Would you like to search another city? (yes or no) "))
    if newCity == "no":
        break
print("Have a good day!")

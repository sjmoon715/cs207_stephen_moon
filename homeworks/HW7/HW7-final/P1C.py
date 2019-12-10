from Markov import *
# Importing operator for max() function to find most common weather outcome
import operator

# I know this isn't the most efficient way to demo the prediction model,
# but this was the first way I thought to do it, and I'm in a bit of a time crunch right now

# New York
# Instatiating New York Weather Markov object
new_york_weather = Markov('rainy')
new_york_weather.load_data("weather.csv")
# Initializing empty dictionary for weather count
new_york_weather_dict = {}
# Making list of keys and values so that I can iterate in for loop
# Keys and values will be the same for every city
key_list = list(new_york_weather.weathers.keys())
val_list = list(new_york_weather.weathers.values())
new_york_weathers = new_york_weather.get_weather_for_day(7,100)
# For each type of weather, the for loop counts occurences and adds them to weather dictionary
for i in range(len(new_york_weather.weathers)):
    new_york_count = new_york_weathers.count(key_list[val_list.index(i)])
    new_york_weather_dict.update({key_list[val_list.index(i)]: new_york_count})
print('New York: ' + str(new_york_weather_dict))

# Chicago
# Instatiating Chicago Weather Markov object
chicago_weather = Markov('snowy')
chicago_weather.load_data("weather.csv")
# Initializing empty dictionary for weather count
chicago_weather_dict = {}
chicago_weathers = chicago_weather.get_weather_for_day(7,100)
# For each type of weather, the for loop counts occurences and adds them to weather dictionary
for i in range(len(chicago_weather.weathers)):
    # Key and val list are same for every city
    chicago_count = chicago_weathers.count(key_list[val_list.index(i)])
    chicago_weather_dict.update({key_list[val_list.index(i)]: chicago_count})
print('Chicago: ' + str(chicago_weather_dict))

# Seattle
# Instatiating Seattle Weather Markov object
seattle_weather = Markov('rainy')
seattle_weather.load_data("weather.csv")
# Initializing empty dictionary for weather count
seattle_weather_dict = {}
seattle_weathers = seattle_weather.get_weather_for_day(7,100)
# For each type of weather, the for loop counts occurences and adds them to weather dictionary
for i in range(len(seattle_weather.weathers)):
    # Key and val list are same for every city
    seattle_count = seattle_weathers.count(key_list[val_list.index(i)])
    seattle_weather_dict.update({key_list[val_list.index(i)]: seattle_count})
print('Seattle: ' + str(seattle_weather_dict))

# Boston
# Instatiating Boston Weather Markov object
boston_weather = Markov('hailing')
boston_weather.load_data("weather.csv")
# Initializing empty dictionary for weather count
boston_weather_dict = {}
boston_weathers = boston_weather.get_weather_for_day(7,100)
# For each type of weather, the for loop counts occurences and adds them to weather dictionary
for i in range(len(boston_weather.weathers)):
    # Key and val list are same for every city
    boston_count = boston_weathers.count(key_list[val_list.index(i)])
    boston_weather_dict.update({key_list[val_list.index(i)]: boston_count})
print('Boston: ' + str(boston_weather_dict))

# Miami
# Instatiating Miami Weather Markov object
miami_weather = Markov('windy')
miami_weather.load_data("weather.csv")
# Initializing empty dictionary for weather count
miami_weather_dict = {}
miami_weathers = miami_weather.get_weather_for_day(7,100)
# For each type of weather, the for loop counts occurences and adds them to weather dictionary
for i in range(len(miami_weather.weathers)):
    # Key and val list are same for every city
    miami_count = miami_weathers.count(key_list[val_list.index(i)])
    miami_weather_dict.update({key_list[val_list.index(i)]: miami_count})
print('Miami: ' + str(miami_weather_dict))

# Los Angeles
# Instatiating Los Angeles Weather Markov object
LA_weather = Markov('cloudy')
LA_weather.load_data("weather.csv")
# Initializing empty dictionary for weather count
LA_weather_dict = {}
LA_weathers = LA_weather.get_weather_for_day(7,100)
# For each type of weather, the for loop counts occurences and adds them to weather dictionary
for i in range(len(LA_weather.weathers)):
    # Key and val list are same for every city
    LA_count = LA_weathers.count(key_list[val_list.index(i)])
    LA_weather_dict.update({key_list[val_list.index(i)]: LA_count})
print('Los Angeles: ' + str(LA_weather_dict))

# San Francisco
# Instatiating San Francisco Weather Markov object
SF_weather = Markov('windy')
SF_weather.load_data("weather.csv")
# Initializing empty dictionary for weather count
SF_weather_dict = {}
SF_weathers = SF_weather.get_weather_for_day(7,100)
# For each type of weather, the for loop counts occurences and adds them to weather dictionary
for i in range(len(SF_weather.weathers)):
    # Key and val list are same for every city
    SF_count = SF_weathers.count(key_list[val_list.index(i)])
    SF_weather_dict.update({key_list[val_list.index(i)]: SF_count})
print('San Francisco: ' + str(SF_weather_dict))

prediction_dict = {}
# Found this line of code on stack oveerflow
new_york_prediction = max(new_york_weather_dict.items(), key=operator.itemgetter(1))[0]
chicago_prediction = max(chicago_weather_dict.items(), key=operator.itemgetter(1))[0]
seattle_prediction = max(seattle_weather_dict.items(), key=operator.itemgetter(1))[0]
boston_prediction = max(boston_weather_dict.items(), key=operator.itemgetter(1))[0]
miami_prediction = max(miami_weather_dict.items(), key=operator.itemgetter(1))[0]
LA_prediction = max(LA_weather_dict.items(), key=operator.itemgetter(1))[0]
SF_prediction = max(SF_weather_dict.items(), key=operator.itemgetter(1))[0]

print('\nMost likely weather in seven days\n----------------------------------')
print("New York: " + str(new_york_prediction))
print("Chicago: " + str(chicago_prediction))
print("Seattle: " + str(seattle_prediction))
print("Boston: " + str(boston_prediction))
print("Miami: " + str(miami_prediction))
print("Los Angeles: " + str(LA_prediction))
print("San Francisco: " + str(SF_prediction))
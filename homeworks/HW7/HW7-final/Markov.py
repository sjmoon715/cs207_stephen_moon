import numpy as np

class Markov:
    def __init__(self, day_zero_weather = None):
        self.data = np.empty([6,6])
        self.weathers = {'sunny':0,'cloudy':1, 'rainy':2, 'snowy':3, 'windy':4, 'hailing':5}
        self.day_zero_weather = day_zero_weather
        self._current_day = 0
        self._current_day_weather = self.day_zero_weather

    def load_data(self, array):
        self.data = np.genfromtxt(open(array,'r'), dtype=None, delimiter=',')

    def get_prob(self, current_day_weather, next_day_weather): 
        if current_day_weather.lower() not in self.weathers.keys() or next_day_weather.lower() not in self.weathers.keys():
            raise Exception("Please enter a different type of weather")
        else:
            next_day_weather_prob = self.data[self.weathers[current_day_weather], self.weathers[next_day_weather]]
            return next_day_weather_prob

    def __iter__(self):
        return self

    def __next__(self):
        # Initalizes list of weathers
        weathers_list = list(self.weathers.keys())
        # Randomly selects a weather with probabilites given by rows of transition matrix
        # Accesses appropriate row of transition matrix using values from 'weathers' dictionary
        self._current_day_weather = np.random.choice(weathers_list, p=self.data[self.weathers[self._current_day_weather]])
        self._current_day += 1
        return self._current_day_weather

    def _simulate_weather_for_day(self, day):
        if day == 0:
            return self._current_day_weather
        else:
            for i in range(day): 
                # Runs __next__() method for specified number of days         
                simulated_weather = self.__next__()
            # Returns weather on last day specified
            return simulated_weather

    def reset_weather(self):
        self._current_day = 0
        self._current_day_weather = self.day_zero_weather
        return self

    def get_weather_for_day(self, day, trials=1):
        predicted_weathers = []
        # For number of trials, append predicted weather to predicted_weathers list
        for i in range(trials):
            predicted_weather = self._simulate_weather_for_day(day)
            predicted_weathers.append(predicted_weather)
            Markov.reset_weather(self)
        return predicted_weathers

# weather_today = Markov("sunny")
# weather_today.load_data('weather.csv') 
# print(weather_today._simulate_weather_for_day(3))
# print(weather_today.get_prob('sunny', 'cloudy'))
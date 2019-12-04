import Markov 
from Markov import Markov

demo = Markov()
demo.load_data("weather.csv")
print(demo.get_prob('cloudy','windy'))
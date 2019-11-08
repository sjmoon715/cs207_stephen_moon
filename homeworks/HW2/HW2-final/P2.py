from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

def languages(filename):
	lineList = list()
	with open(filename) as f:
		for line in f:
			lineList.append(line)
			lineList = [line.rstrip('\n') for line in lineList]
	languages = Counter(lineList)
	for i in languages:
		print("{}: {}".format(i,languages[i]))
	
	return(languages)

filename = "languages.txt"
final_count = languages(filename)

x_coords = np.arange(0, 8, 1)
freqs = final_count.values()
labels = final_count.keys()

plt.bar(x_coords, freqs)
plt.xticks(x_coords, labels)

plt.show()


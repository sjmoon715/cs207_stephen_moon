import math

def counter(f):
	def inner_function(i,j):
		inner_function.counter += 1
		return f(i,j)
	inner_function.counter = 0
	return inner_function

@counter
def pyt(a,b):
	a = a
	b = b
	c = math.sqrt((a**2)+(b**2))
	return c
	
a = [3,4,5]
b = [4,5,6]

for a,b in zip(a,b):
	print pyt(a,b)
	print pyt.counter

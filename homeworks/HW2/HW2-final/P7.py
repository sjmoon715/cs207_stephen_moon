import math

def positivity(func):
    d = 0.0
    def inner(*args):
        if func(*args) < d:
            raise ValueError('Negative Quantity')
        return func(*args)
    return inner

@positivity
def discriminant(a,b,c):
    d = b**2 - 4*a*c
    return d
@positivity
def abs_val(x):
    if x<0:
        return -1*x
    else:
        return x
@positivity
def pythagorean(a,b):
    c = math.sqrt(a**2 + b**2)
    return c

print("** Cannot violate positivity for two of my three functions **")

try:
    print("Absolute Value of 4 = {}".format(abs_val(4)))
    print("Pythagorean Theorem with a = 2, b = 4: c = {}".format(pythagorean(2,4)))
    print("Discriminant with a = 1, b = 5, c = 2: d = {}".format(discriminant(1,5,2)))
    print("Absolute Value of -3 = {}".format(abs_val(-3)))
    print("Pythagorean Theorem with a = 3, b = 8: c = {}".format(pythagorean(3,8)))
    print("Discriminant with a = 1, b = 5, c = 2: d = {}".format(discriminant(4,2,3)))
except ValueError:
    print("Caught ValueError as expected!")

    



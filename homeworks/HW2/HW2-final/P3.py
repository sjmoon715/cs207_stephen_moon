import math
from collections import Counter

circle_radii = list()
with open("circles.txt") as f:
    for line in f:
        radius = float(line)
        circle_radii.append(radius)

def circle_area(r):
    a = math.pi*(r**2)
    return(a) 

def my_ave(radii, circle_area):
    radii = radii
    circle_areas = list(map(circle_area, circle_radii))
    number_of_circles = len(circle_radii)
    total_area = math.fsum(circle_areas)
    average = total_area/number_of_circles
    return average
    
my_average = my_ave(circle_radii, circle_area)

print("My avg : {}".format(my_average))


import math
from collections import Counter
import numpy as np
import time

def timer(f):
    def inner(*args):
        t0 = time.time()
        output = f(*args)
        elapsed = time.time() - t0
        print("Time Elapsed: {}".format(elapsed))
        return output
    return inner

circle_radii = list()
with open("circles.txt") as f:
    for line in f:
        radius = float(line)
        circle_radii.append(radius)

areas_list = [0.0]*len(circle_radii)
areas_np = np.zeros(len(circle_radii))

for i in range(len(circle_radii)):
    r = circle_radii[i]
    area = math.pi*r**2
    areas_list[i] = area
    areas_np[i] = area

@timer
def my_ave(areas_list):
    areas_list = areas_list
    number_of_circles = len(areas_list)
    area_sum = math.fsum(areas_list)
    average = area_sum/number_of_circles
    return average

@timer
def np_ave(areas_np):
    areas_np = areas_np
    avg_area = np.average(areas_np)
    return avg_area

print("Speed Test: ")
print("My avg : {} \n".format(my_ave(areas_list)))
print("Np avg : {}".format(np_ave(areas_np)))



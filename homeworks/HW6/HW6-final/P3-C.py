import P2
from P2 import Heap, MaxHeap, MinHeap
import P3
from P3 import PriorityQueue, NaivePriorityQueue, HeapPriorityQueue, PythonPriorityQueue

from random import sample
from time import time
import heapq
import numpy as np
import matplotlib.pyplot as plt

ns = (10, 20, 50, 100, 200, 500)

naive_queue = P3.timeit(pqclass=NaivePriorityQueue, n_average = 5)
heap_queue = P3.timeit(pqclass=HeapPriorityQueue, n_average = 5)
python_queue = P3.timeit(pqclass=PythonPriorityQueue, n_average = 5)

plt.plot(ns, naive_queue)
plt.plot(ns, heap_queue)
plt.plot(ns, python_queue)
plt.title("Runtime for mergesortedlists Method")
plt.ylabel("Runtime")
plt.xlabel("Merged Lists")
plt.legend(["NaivePriorityQueue", "HeapPriorityQueue", "PythonPriorityQueue"])
plt.show()
from random import sample
from time import time
import P2 as p2
from P2 import Heap, MaxHeap, MinHeap
import heapq

class PriorityQueue:
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def __len__(self):
        return len(self.elements)

    def __bool__(self):
        return len(self.elements) > 0

    def put(self, val):
        raise NotImplementedError # Implemented in derived classes

    def get(self):
        raise NotImplementedError # Implemented in derived classes

    def peek(self):
        raise NotImplementedError # Implemented in derived classes

class NaivePriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def put(self, val):
        if len(self.elements) > self.max_size:
            raise IndexError("Full Priority Queue")
        else:
            self.elements.append(val)

    def get(self):
        if len(self.elements) == 0:
            raise IndexError("Empty Priority Queue")
        else:
            min_node = min(self.elements)
            self.elements.remove(min_node)
            return min_node
    
    def peek(self):
        if len(self.elements) == 0:
            raise IndexError("Empty Priority Queue")
        else:
            min_node = min(self.elements)
            return min_node

class HeapPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        self.elements = MinHeap([])
        self.max_size = max_size
    def put(self, val):
        if len(self.elements) > self.max_size:
            raise IndexError("Full Priority Queue")
        else:
            self.elements.heappush(val)
    def get(self):
        if not self.elements:
            raise IndexError("Empty Priority Queue")
        else:
            return self.elements.heappop()
    def peek(self):
        if not self.elements:
            raise IndexError("Empty Priority Queue")
        else:
            return self.elements.elements[0]

class PythonPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size
    def put(self, val):
        if len(self.elements) > self.max_size:
            raise IndexError("Full Priority Queue")
        else:
            heapq.heappush(self.elements, val)
    def get(self):
        if not self.elements:
            raise IndexError("Empty Priority Queue")
        else:
            return heapq.heappop(self.elements)
    def peek(self):
        if not self.elements:
            raise IndexError("Empty Priority Queue")
        else:
            return self.elements[0]

def mergesortedlists(lists, pqclass=PriorityQueue):
    merged = []
    pq = pqclass(len(lists))
    for i, l in enumerate(lists): 
        pq.put((l.pop(0), i))

    while pq:
        ele, i = pq.get()
        merged.append(ele)
        if lists[i]:
            pq.put((lists[i].pop(0), i)) 

    return merged

def generatelists(n, length=20, dictionary_path='../data/words.txt'):
    with open(dictionary_path, 'r') as f:
        words = [w.strip() for w in f.readlines()]
    lists = []
    for _ in range(n):
        lists.append(sorted(sample(words, length)))
    return lists

def timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=PriorityQueue, n_average=5):
    elapsed = []
    for n in ns:
        timeaccum = 0
        for _ in range(n_average):
            lists = generatelists(n)
            start = time()
            merged = mergesortedlists(lists, pqclass)
            end   = time()
            timeaccum += end-start
        elapsed.append(timeaccum / n_average)
    return elapsed
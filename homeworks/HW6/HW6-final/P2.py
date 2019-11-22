from math import floor
from typing import List

class Heap:
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.build_heap()

    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1

    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        if self.size == 0:
            return '\\--'
        elif idx < self.size:
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                    self.to_string(new_prefix, self.left(idx), True) + \
                    self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> str:
        return self.size
    
    def compare(self, a: int, b: int) -> bool:
        # Implemented in child classes
        pass

    def heapify(self, idx: int) -> None:
        current_node = idx
        left_node = self.left(idx)
        right_node = self.right(idx)
        # Checks whether node is in range and compares current node with left node
        if left_node < self.size and self.compare(self.elements[current_node], self.elements[left_node]):
            current_node = left_node
        # Checks whether node is in range and compares current node with right node
        if right_node < self.size and self.compare(self.elements[current_node], self.elements[right_node]):
            current_node = right_node
        if current_node != idx:
            self.swap(current_node, idx)
            # To make the method recursive
            self.heapify(current_node)

    def build_heap(self) -> None:
        initial_idx = floor(self.size/2 - 1)
        for i in range(initial_idx, -1, -1):
            self.heapify(i)
    
    # Found the implementation for this helper function online
    def siftup(self, idx: int) -> None:
        if idx != 0:
            parent_node = self.parent(idx)
            if self.compare(self.elements[parent_node], self.elements[idx]):
                self.swap(parent_node, idx)
                self.siftup(parent_node)

    def heappush(self, key: int) -> None:
        self.size += 1
        self.elements.append(key)
        self.siftup(self.size - 1)
        
    def heappop(self) -> int:
        if self.size:
            self.swap(0, self.size - 1)
            self.size -= 1
            self.heapify(0)
            return self.elements.pop()
        else:
            raise IndexError("Outside of index")

class MinHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        if a > b:
            return True
        else:
            return False

class MaxHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        if a < b:
            return True
        else:
            return False
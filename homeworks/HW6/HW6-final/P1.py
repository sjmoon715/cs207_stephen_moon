from enum import Enum

class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left ).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if node == None: 
            return BSTNode(key, val)
        if key < node.key:
            node.left  = self._put(node.left,  key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if   key < node.key:
            return self._get(node.left,  key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val
    
    def _removemin (self, node):
        if not node.left:
            return None
        else:
            node.left = self._removemin(node.left)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node
    
    def min_node(self, node):
        if not node.left:
            return (node.key, node.val)
        else:
            return self.min_node(node.left)

    def remove(self, key):
        self._root = self._remove(self._root, key)

    def _remove(self, node, key):
        if not node:
            raise KeyError("Could not find key.")
        elif key == node.key:
            if not node.left and not node.right:
                return None
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            elif node.left != None and node.right != None:
                node.key, node.val = self.min_node(node.right)
                node.right = self._removemin(node.right)
        elif key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)

        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node
            
    @staticmethod
    def _size(node):
        return node.size if node else 0

class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

class DFSTraversal():
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):
        self.tree = tree
        self.traversalType = traversalType
        self.nodes = []
        self.index = 0
        if traversalType == DFSTraversalTypes.INORDER:
            self.inorder(tree)
        elif traversalType == DFSTraversalTypes.PREORDER:
            self.preorder(tree)
        elif traversalType == DFSTraversalTypes.POSTORDER:
            self.postorder(tree)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            node = self.nodes[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return node

    def inorder(self, bst: BSTTable):
        node = bst._root
        stack = []
        while True:
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                self.nodes.append(node)
                node = node.right
            else:
                break

    def preorder(self, bst: BSTTable):
        stack = [bst._root]
        while stack:
            node = stack.pop()
            self.nodes.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def postorder(self, bst: BSTTable):
        stack = [bst._root]
        while stack:
            node = stack.pop()
            self.nodes.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        self.nodes = self.nodes[::-1]
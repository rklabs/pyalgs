from __future__ import print_function

import random
import time


class Node(object):

    def __init__(self, value, left, right):
        self._value = value
        self._left = left
        self._right = right


class BinaryTree(object):

    def __init__(self):
        self._root = None
        self._inorder_list = []
        self._preorder_list = []
        self._postorder_list = []

    def _preorder(self, root):
        if root:
            self._preorder_list.append(root._value)
            self._preorder(root._left)
            self._preorder(root._right)

    def preorder(self):
        self._preorder(self._root)

    def _inorder(self, root):
        if root:
            self._inorder(root._left)
            self._inorder_list.append(root._value)
            self._inorder(root._right)

    def inorder(self):
        self._inorder(self._root)

    def _postorder(self, root):
        if root:
            self._postorder(root._left)
            self._postorder(root._right)
            self._postorder_list.append(root._value)

    def postorder(self):
        self._postorder(self._root)

    def _insert_iterative(self, val, root):
        while root:
            slot = root
            if val < root._value:
                root = root._left
            elif val > root._value:
                root = root._right

        if val < slot._value:
            slot._left = Node(val, None, None)
        elif val > slot._value:
            slot._right = Node(val, None, None)

    def _insert_recursive(self, val, root):
        if root is None:
            return Node(val, None, None)

        if val < root._value:
            root._left = self._insert_recursive(val, root._left)
        elif val > root._value:
            root._right = self._insert_recursive(val, root._right)

        return root

    def insert(self, val, insertionMethod="recursive"):
        if self._root is None:
            self._root = Node(val, None, None)
            return

        if insertionMethod == "recursive":
            if val < self._root._value:
                self._root._left = \
                    self._insert_recursive(val, self._root._left)
            elif val > self._root._value:
                self._root._right = \
                    self._insert_recursive(val, self._root._right)
        elif insertionMethod == "iterative":
            self._insert_iterative(val, self._root)


if __name__ == '__main__':
    btree = BinaryTree()

    random.seed(time.time())

    million = 1000000

    elems = random.sample(range(million * 10), million)
    start = time.time()

    for elem in elems:
        btree.insert(elem, insertionMethod="recursive")

    end = time.time() - start

    print("recursive")
    print("time taken to insert million random numbers {}s".format(end))

    btree.preorder()
    btree.inorder()
    btree.postorder()

    btree1 = BinaryTree()

    start = time.time()

    for elem in elems:
        btree1.insert(elem, insertionMethod="iterative")

    end = time.time() - start

    print("iterative")
    print("time taken to insert million random numbers {}s".format(end))
    btree1.preorder()
    btree1.inorder()
    btree1.postorder()

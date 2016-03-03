#!/usr/bin/env python
from collections import deque
from collections import defaultdict


class Graph(object):
    def __init__(self, noOfNodes):
        self._noOfNodes = noOfNodes
        self._adjV = defaultdict()
        self._stack = deque()
        self._visited = []

    def addEdge(self, v, w):
        self._adjV.setdefault(v, []).append(w)

    def _toposort(self, vertex):
        pass

    def toposort(self):
        pass

if __name__ == '__main__':
    graph = Graph(5)

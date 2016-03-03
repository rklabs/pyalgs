#!/usr/bin/env python
from collections import deque
from collections import defaultdict


class Graph(object):
    def __init__(self, noOfVertices):
        self._noOfVertices = noOfVertices
        self._adjV = defaultdict()
        self._visited = []

    def addEdge(self, vertex, neighbor):
        self._adjV.setdefault(vertex, []).append(neighbor)

    def _dfs(self, startV):
        self._visited[startV] = True

        vq = deque()
        vq.appendleft(startV)

        while vq:
            vertex = vq.popleft()

            print vertex

            for adjV in self._adjV[vertex]:
                if not self._visited[adjV]:
                    self._visited[adjV] = True
                    vq.appendleft(adjV)

    def dfs(self):
        for _ in range(self._noOfVertices):
            self._visited.append(False)

        for vertex in range(self._noOfVertices):
            if not self._visited[vertex]:
                self._dfs(vertex)

if __name__ == '__main__':
    graph = Graph(5)
    graph.addEdge(0, 2)
    graph.addEdge(0, 3)
    graph.addEdge(1, 0)
    graph.addEdge(2, 1)
    graph.addEdge(3, 4)
    graph.addEdge(4, 0)

    graph.dfs()

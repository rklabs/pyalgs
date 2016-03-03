#!/usr/bin/env python
from collections import deque
from collections import defaultdict


class Graph(object):
    def __init__(self, noOfNodes):
        self._noOfNodes = noOfNodes  # No. of nodes in the graph
        self._adjV = defaultdict()  # Dictionary of vertices and adjacencies

    def addEdge(self, vertex, neighbor):
        self._adjV.setdefault(vertex, []).append(neighbor)

    def bfs(self, startV):
        vq = deque()

        visited = []
        for _ in range(self._noOfNodes):
            visited.append(False)

        visited[startV] = True
        vq.append(startV)

        while vq:
            vertex = vq.popleft()

            print vertex,

            for adjV in self._adjV[vertex]:
                if not visited[adjV]:
                    visited[adjV] = True
                    vq.append(adjV)


if __name__ == '__main__':
    graph = Graph(5)
    graph.addEdge(0, 2)
    graph.addEdge(0, 3)
    graph.addEdge(1, 0)
    graph.addEdge(2, 1)
    graph.addEdge(3, 4)
    graph.addEdge(4, 0)

    graph.bfs(0)

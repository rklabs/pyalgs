#!/usr/bin/env python
from collections import defaultdict


class Graph(object):
    def __init__(self, vertices):
        self._vertices = vertices
        self._adjacencies = defaultdict()

    def addEdge(self, vertex, neighbor):
        self._adjacencies.setdefault(vertex, []).append(neighbor)

    def _dfs(self, start_vertex, visited):
        visited[start_vertex] = True
        print(start_vertex)

        for v in self._adjacencies[start_vertex]:
            if not visited[v]:
                visited[v] = True
                self._dfs(v, visited)

    def dfs(self, start_vertex):
        visited = []
        for _ in range(self._vertices):
            visited.append(False)

        visited[start_vertex] = True

        self._dfs(start_vertex, visited)

if __name__ == '__main__':
    graph = Graph(5)
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 2)
    graph.addEdge(1, 4)
    graph.addEdge(2, 0)
    graph.addEdge(2, 3)
    graph.addEdge(3, 3)
    graph.addEdge(4, 1)

    graph.dfs(2)

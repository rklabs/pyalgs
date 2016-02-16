from collections import defaultdict

class Graph(object):
    def __init__(self, noOfVertices):
        self._noOfVertices = noOfVertices
        self._adjV = defaultdict()

    def addEdge(self, vertex, neighbor):    
        self._adjV.setdefault(vertex, []).append(neighbor)

    def _dfs(self, startV, visited):
        visited[startV] = True
        print startV
        
        for v in self._adjV[startV]:
            if not visited[v]:
                visited[v] = True
                self._dfs(v, visited)

    def dfs(self, startV):
        visited = []
        for _ in range(self._noOfVertices):
            visited.append(False)
    
        visited[startV] = True
        
        self._dfs(startV, visited)
                    
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

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)

g = Graph()
v = int(input("\nEnter no. of vertices: "))
print("\nEnter x to stop")
edge = input("\nEnter edge: ")
while edge != 'x':
    a,b = list(map(int,edge.split()))
    g.addEdge(a,b)
    edge = input("Enter edge: ")
s = int(input("\nEnter starting vertex: "))
print("\nFollowing is DFS from (starting from vertex {})\n".format(s))
g.DFS(s)

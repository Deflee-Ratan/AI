from collections import defaultdict
import queue


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def BFS(self,s):
        visited = [False]*(max(self.graph)+1)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s,end=" ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

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
g.BFS(s)

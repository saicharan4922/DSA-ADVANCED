# Breadth First Traversal for a Graph
from collections import defaultdict 
class Graph: 
   
    def __init__(self): 
        self.graph = defaultdict(list) 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
        visited = [False] * (max(self.graph) + 1) 
        queue = [] 
        queue.append(s) 
        visited[s] = True
  
        while queue: 
            s = queue.pop(0) 
            print (s, end = " ") 
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print("BFS starting from vertex 2:")
g.BFS(2)


# Depth First Traversal for a Graph

from collections import defaultdict 
  
class Graph: 
   
    def __init__(self): 
        self.graph = defaultdict(list) 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
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
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print("DFS starting from vertex 2:")
g.DFS(2)


# Count the number of nodes at given level in a tree using BFS:

from collections import defaultdict 
  
class Graph: 
   
    def __init__(self): 
        self.graph = defaultdict(list) 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s, level): 
        visited = [False] * (max(self.graph) + 1) 
        queue = [] 
        queue.append(s) 
        visited[s] = True
        count = 0
        depth = 0
  
        while queue: 
            size = len(queue)
            for i in range(size):
                s = queue.pop(0) 
                if depth == level:
                    count += 1
                for i in self.graph[s]: 
                    if visited[i] == False: 
                        queue.append(i) 
                        visited[i] = True
            depth += 1
        return count
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(2, 4) 
g.addEdge(2, 5) 
g.addEdge(3, 6) 
g.addEdge(4, 6) 
g.addEdge(5, 7) 
g.addEdge(7, 8)

print("Number of nodes at level 2 in the tree:")
print(g.BFS(0, 2))


# Count number of trees in a forest:
from collections import defaultdict 
  
class Graph: 
   
    def __init__(self): 
        self.graph = defaultdict(list) 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def DFSUtil(self, v, visited): 
        visited.add(v) 
  
        for neighbour in self.graph[v]: 
            if neighbour not in visited: 
                self.DFSUtil(neighbour, visited) 
  
  
    def countTrees(self): 
        visited = set() 
        count = 0
  
        for i in self.graph: 
            if i not in visited: 
                self.DFSUtil(i, visited) 
                count += 1
  
        return count
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(3, 4) 
g.addEdge(4, 5) 

print("Number of trees in the forest:")
print(g.countTrees())


# Detect Cycle in a Directed Graph:
from collections import defaultdict 
  
class Graph: 
   
    def __init__(self): 
        self.graph = defaultdict(list) 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def isCyclicUtil(self, v, visited, recStack): 
  
        visited[v] = True
        recStack[v] = True
  
        for neighbour in self.graph[v]: 
            if visited[neighbour] == False:
                g = Graph() 
g.addEdge(0, 1) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 

if g.isCyclic() == 1: 
    print("Graph has a cycle") 
else: 
    print("Graph does not have a cycle")
    

'''
Find if there is a path between two vertices in a directed graph
Following is the sample graph representation (vertex: comma seperated adjacent vertex)
0 : 1,2
1 : 2
2 : 0,3
3 : 3
'''
from collections import defaultdict
  
class Graph:
  
    def __init__(self,vertices):
        self.V= vertices 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def printGraph(self):
        print self.graph

    def hasPath(self, start, end):
        visited = set()
        queue = []
        
        queue.append(start)
        visited.add(start)

        while len(queue) != 0:
            current = queue.pop(0)
            if current == end:
                return True
            for adjancent in self.graph[current]:
                if adjancent not in visited:
                    queue.append(adjancent)
                    visited.add(adjancent)

        return False

# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
#g.printGraph()
print g.hasPath(1,3) #True
print g.hasPath(3,1) #False
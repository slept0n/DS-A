"""
1. Create a recursive function that takes the index of the node and a visited array.
2. Mark the current node as visited and print the node.
3. Traverse all the adjacent and unmarked nodes and call the recursive function with the index of the adjacent node."""


"""Path Finding 
We can specialize the DFS algorithm to find a path between two given vertices u and z. 
i) Call DFS(G, u) with u as the start vertex. 
ii) Use a stack S to keep track of the path between the start vertex and the current vertex. 
iii) As soon as destination vertex z is encountered, return the path as the 
contents of the stack  """


# Python program to print DFS traversal
# from a given given graph
from collections import defaultdict
  
# This class represents a directed graph using
# adjacency list representation
  
  
class Graph:
  
    # Constructor
    def __init__(self):
  
        # default dictionary to store graph
        self.graph = defaultdict(list)
  
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
  
    # A function used by DFS
    def DFSUtil(self, v, visited):
  
        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')
  
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
  
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):
  
        # Create a set to store visited vertices
        visited = set()
  
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)
  
# Driver code
  
  
# Create a graph given
# in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
  
print("Following is DFS from (starting from vertex 2)")
g.DFS(2)
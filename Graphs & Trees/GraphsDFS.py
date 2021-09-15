""" we can represent a graph using a hashtable/dictionary. this is called an adjacency list. """

flight5125 = {
    '1' : ['DTW', 'CHI'],
    '2' : ['CHI', 'HNL'],
    '3' : ['HNL', 'LAX'],
}

# we can now check the flight number and see all of its connecting flights.
# we can visualize this as a big graph where every location is connecting in some way.



# Python3 program to print DFS traversal
# from a given given graph
from collections import defaultdict
 
# This class represents a directed graph using
# adjacency list representation
 
 
 # DFS CAN BE A RECURSIVE ALGORITHM
 
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

















'''Python program to print DFS traversal for complete graph'''
from collections import defaultdict
 
# this class represents a directed graph using adjacency list representation
 
class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph=defaultdict(list)
     
    # Function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
    # A function used by DFS
    def DFSUtil(self,v,visited):
        # Mark the current node as visited and print it
        visited.add(v)
        print(v)
         
        # recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour,visited)
        # The function to do DFS traversal. It uses recursive DFSUtil
    def DFS(self):
        # create a set to store all visited vertices
        visited=set()
        # call the recursive helper function to print DFS traversal starting from all
        # vertices one by one
        for vertex in list(self.graph):
            if vertex not in visited:
                self.DFSUtil(vertex,visited)
# Driver code
# create a graph given in the above diagram
 
g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
g.DFS()
 







""" ANOTHER WAY TO IMPLEMENT DFS ON A DICTIONARY OF ADJENCENYS"""



# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')

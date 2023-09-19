class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = []

    def addEdge(self, u,v,w):
        self.graph.append([u,v,w])
    
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.vertices):
            print("{0}\t\t{1}".format(i, dist[i]))
            
    
    def BellmanFord(self, src):
        dist = [float("Inf")]* self.vertices
        dist[src] = 0
        
        for _ in range(self.vertices-1):
            for u,v,w in self.graph:
                if (dist[u] != float("Inf") and dist[v] > dist[u]+w):
                    dist[v] = dist[u]+w
        
        for u,v,w in self.graph:
            if (dist[u] != float("Inf") and dist[v] > dist[u]+w):
                print("Negative cycle bro")
                return
        self.printArr(dist)
    
g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

# function call
g.BellmanFord(0)
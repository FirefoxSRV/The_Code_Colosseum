# Time Complexity: The time complexity of Dijkstra’s algorithm is O(V^2). This is because the algorithm uses two nested loops to traverse the graph and find the shortest path from the source node to all other nodes.

# Space Complexity: The space complexity of Dijkstra’s algorithm is O(V), where V is the number of vertices in the graph. This is because the algorithm uses an array of size V to store the distances from the source node to all other nodes.




class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = [[0 for i in range(self.vertices)] for j in range(self.vertices)]
    
    def printSoln(self,dist):
        for _ in range(self.vertices):
            print(_,"\t",dist[_])
    
    def minDistance(self,dist,sptSet):
        min = 1e7
        for _ in range(self.vertices):
            if sptSet[_] == False and dist[_] < min:
                min = dist[_]
                min_ind = _
        return min_ind
    
    def Dijisktras(self,vertex):
        dist = [1e7] * self.vertices
        dist[vertex] = 0
        sptSet = [False] * self.vertices
        
        for cout in range(self.vertices):
            u = self.minDistance(dist,sptSet)
            
            sptSet[u]=True
            # print(u)
            for v in range(self.vertices):
                if(sptSet[v] == False and self.graph[u][v]>0 and dist[v]>dist[u]+self.graph[u][v]):    #[u][v] > 0 because edge must exist
                    dist[v] = dist[u]+self.graph[u][v]
                    
        self.printSoln(dist)
            

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
 
g.Dijisktras(0)


# For prims, its very similar to dijikstra - just add another array called parent
# parent = [None]*self.vertices 
# parent[0]=-1 
# inside 2nd for loop,
# parent[v]=u 
# print parent

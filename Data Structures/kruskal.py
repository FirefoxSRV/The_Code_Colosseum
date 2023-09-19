        
# Time Complexity: O(E * logE) or O(E * logV) 
# Sorting of edges takes O(E * logE) time. 
# After sorting, we iterate through all edges and apply the find-union algorithm. The find and union operations can take at most O(logV) time.
# So overall complexity is O(E * logE + E * logV) time. 
# The value of E can be at most O(V2), so O(logV) and O(logE) are the same. Therefore, the overall time complexity is O(E * logE) or O(E*logV)


# Auxiliary Space:
# O(V + E), where V is the number of vertices and E is the number of edges in the graph.

class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph=[]
    
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    
    def find(self,parent,x):
        if(parent[x] != x):   # If parent is itself
            parent[x] = self.find(parent,parent[x])
        return parent[x]


    def union(self,parent,rank,x,y):
        if(rank[x] < rank[y]):
            parent[x] = y
        elif (rank[x] > rank[y]):
            parent[y] = x
        else:
            parent[x] = y
            rank[y] = rank[y] + 1
    
    def KruskalMST(self):
        result = []
        
        for i in range(len(self.graph)):
            for j in range(len(self.graph) - i - 1):
                if(self.graph[j][2] > self.graph[j+1][2]):
                    self.graph[j],self.graph[j+1] = self.graph[j+1],self.graph[j]   # sort based on ascending order of weights
        
        parent = []
        rank = []
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
        # parent is now [0 to n]
        # rank is [0 0 0 ....0]
        e=0
        i=0
        while e<self.vertices-1:   # not putting -1 can cause index out of range and number of edges = num of vertices - 1
            u,v,w = self.graph[i]
            i=i+1
            x=self.find(parent,u)
            y=self.find(parent,v)

            if(x!=y):       # no cycling Shrey ;)
                e=e+1
                result.append([u,v,w])
                self.union(parent,rank,x,y)
        min=0
        for u,v,w in result:
            min+=w
            print([u,v,w])
        print("Weight is ", min)
        
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
g.KruskalMST()


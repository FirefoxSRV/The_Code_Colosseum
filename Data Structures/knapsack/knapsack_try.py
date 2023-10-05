

def knapsack(weights,values,capacity):
    n = len(weights)
    matrix = [[0]* (capacity+1) for _ in range(len(weights)+1)]
    
    for i in range(1, n+1):
        for w in range(1,capacity+1):
            if (weights[i-1]>w):
                matrix[i][w] = matrix[i-1][w]
            else:
                matrix[i][w] = max(matrix[i-1][w] , matrix[i-1][ w - weights [i-1] ] +values[i-1])
    
    finalArray=[]
    i,j = n,capacity
    while i>0 and j>0:
        if (matrix[i][j] != matrix[i-1][j]):
            finalArray.append(i-1)
            j -= weights[i-1]
        i-=1
        
    finalArray.reverse()
    return matrix[n][capacity],finalArray
        
     


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_value, selected_items = knapsack(weights, values, capacity)
print("Maximum Value:", max_value)
print("Selected Items:", selected_items)

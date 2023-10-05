def knapsack(items,capacity):
    items.sort(key=lambda x: x[1]/x[0],reverse = True)
    totalValue = 0
    knapsack = []
    for weight,value in items:
        if (capacity <= 0):
            return None
        elif (weight <= capacity):
            totalValue += value
            knapsack.append([weight,value])
            capacity-=weight
        # else:
        #     fraction = capacity/weight
        #     totalValue = fraction*value
        #     knapsack.append([weight,fraction])
            # capacity=0

    return totalValue,knapsack





items = [(2, 10), (3, 5), (5, 15), (7, 7), (1, 6)]
capacity = 15

max_value, selected_items = knapsack(items, capacity)
print("Maximum Value:", max_value)
print("Selected Items (Weight, Fraction):", selected_items)
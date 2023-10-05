class Node:
    def __init__(self,alphabet,count,combinedNode = None):
        self.alphabet = alphabet
        self.count = count
        self.zero = None
        self.one = None

def combine(sorted_list,object_list):
    if len(sorted_list) > 1:
        totalCount = sorted_list[0]['count'] + sorted_list[1]['count']
        node1 = Node(sorted_list[0]['alphabet'],sorted_list[0]['count'])
        node2 = Node(sorted_list[1]['alphabet'],sorted_list[1]['count'])
        object_list.append(node1)
        object_list.append(node2)
        combinedNode = Node('-',totalCount)
        combinedNode.zero=node1
        combinedNode.one=node2
        removal1 = sorted_list[0]
        removal2 = sorted_list[1]
        sorted_list.remove(removal1)
        sorted_list.remove(removal2)
        object_list.remove(node1)
        object_list.remove(node2)
        object_list.append(combinedNode)
        obj = {'alphabet':combinedNode.alphabet,'count':combinedNode.count}
        sorted_list.append(obj)
        sorted_list = sorted(sorted_list[2:] + [obj], key=lambda x: x['count'])
        return object_list
            
            
    if len(sorted_list) == 1:
        return 0



string = input()
dict = {}
for i in string:
    if (i in dict):
        dict[i] +=1
    else:
        dict[i] = 1
list=[]
for i in dict:
    list.append({'alphabet':i,'count':dict[i]})
    
sorted_list = sorted(list, key=lambda dict:dict['count'])
object_list = [] 
print(sorted_list)
c = 0
while True:
    returner = combine(sorted_list, object_list)
    combinedNode = returner
    if(returner):
        c = returner
        print(sorted_list)
    else:
        break

print(c)
c = c[::-1]
print(c[0].zero.alphabet)
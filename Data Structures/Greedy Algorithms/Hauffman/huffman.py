class Huffman:
    def __init__(self,symbol,frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

def build_tree(data):
    counter = {}
    for i in data:
        if (i in counter):
            counter[i] +=1
        else:
            counter[i] = 1
    nodes = [Huffman(symbol,frequency) for symbol,frequency in counter.items()]
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.frequency)
        left_node = nodes.pop(0)
        right_node = nodes.pop(0)
        
        merge_node = Huffman(None,left_node.frequency+right_node.frequency)
        merge_node.left = left_node
        merge_node.right = right_node
        nodes.append(merge_node)
    return nodes[0]


def building_code(node,current_code,huffman_codes):
    if (node is None):
        return
    if node.symbol is not None:
        huffman_codes[node.symbol] = current_code
    building_code(node.left,current_code+'0',huffman_codes)
    building_code(node.right,current_code+'1',huffman_codes)

    
def huffman_encoding(data):
    if len(data) == 0:
        return None,None
    node = build_tree(data)
    d = {}
    building_code(node,"",d)
    encodedElement = "".join(d[symbol] for symbol in data)
    return encodedElement,node
    
def huffman_decode(node,encodedElement):
    if node is None or encodedElement is None:
        return None
    decoded_element = ""
    current_node = node
    for i in encodedElement:
        if(i == "0"):
            current_node=current_node.left
        elif(i== "1"):
            current_node=current_node.right
        if (current_node.symbol is not None):
            decoded_element += current_node.symbol
            current_node = node
    print(decoded_element)
    

data = "this is an example for huffman encoding"
encodedElement,node = huffman_encoding(data)
print(encodedElement)
huffman_decode(node,encodedElement)



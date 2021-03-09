class Node:
    def __init__(self, data):
        self.data = data
        self.root = None
        self.left = None
        self.right = None

def search(node):
    global size 
    #print(node.data)
    size += 1

    if node.left != None:
        search(node.left)
    if node.right != None:
        search(node.right)


T = int(input())
for t in range(T):
    v, e, ver1, ver2 = map(int, input().split())
    
    temp = list(map(int, input().split()))
    edges = []
    for i in range(0, len(temp), 2):
        edges.append((temp[i], temp[i + 1]))
    
    nodes = [None] * (v + 1)
    
    for edge in edges:
        a, b = edge

        if nodes[a] == None:
            node = Node(a)
            nodes[a] = node 

        if nodes[b] == None:
            node = Node(b)
            node.root = nodes[a]
            if nodes[a].left == None:
                nodes[a].left = node
            else:
                nodes[a].right = node  
             
            nodes[b] = node 
        else:
            if nodes[a].left == None:
                nodes[a].left = nodes[b]
            else:
                nodes[a].right = nodes[b]
            nodes[b].root = nodes[a] 
        
    
    root1 = []

    root = nodes[ver1].root
    node = root
    while root != None:
        root1.append(root.data)
        root = nodes[node.data].root
        node = root
    root = nodes[ver2].root
    node = root

    root_index = -1

    while root != None:
        if root.data in root1:
            root_index = root.data
            break 
        root = nodes[node.data].root
        node = root 
    
    size = 0
    search(nodes[root_index])
    
    print("#" + str(t + 1), root_index, size)
    
    
    

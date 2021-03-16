class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None 
    
    def insert(self, data):
        self.root = self.insert_value(self.root, data)
        return self.root is not None 
    
    def insert_value(self, node, data):
        if node == None: # 루트가 빈 경우 새로운 노드를 루트로 
            new_node = Node(data)
            node = new_node
        else:
            if data <= node.data: # 데이터보다 작은 경우 왼쪽 자식 
                node.left = self.insert_value(node.left, data)
            else: # 데이터가 큰 경우 오른쪽 자식 
                node.right = self.insert_value(node.right, data)
        return node 
    
    def find(self, data):
        return self.find_value(self.root, data)
    
    def find_value(self, node, data): # 원하는 값의 존재 유무 
        if node == None or node.data == data:
            return node is not None 
        elif node.data <= data: # 큰 경우 오른쪽 탐색 
            return self.find_value(node.right, data)
        else: # 작은 경우 왼쪽 탐색 
            return self.find_value(node.left, data)
        
    def delete(self, data):
        return self.delete_value(self.root, data)
    
    def delete_value(self, node, data):
        if node == None:
            return node, False # 삭제할 데이터가 없다 
        
        is_deleted = False
        if data == node.data: # 삭제할 값을 찾은 경우 
            is_deleted = True
            if node.left == None and node.right == None: # leaf 노드인 경우 
                node = None # 그냥 삭제 
                return node, True 
            else:
                if node.right and not node.left: # 오른쪽 자식만 있는 경우 
                    node = node.right 
                    return node, True 
                elif not node.right and node.left: # 왼쪽 자식만 있는 경우
                    node = node.left 
                    return node, True 
                else: # 둘 다 있는 경우, 오른쪽 자식 노드에서 가장 작은 값, 왼쪽 자식 노드에서 가장 큰 값을 가져온다. 
                    parent, temp = node, node.rigt 
                    while temp.left:
                        parent, temp = temp, temp.left # 왼쪽으로 계속 이동해서 제일 작은 값을 가져온다. 
                    # 오른쪽 자식에서 가장 작은 값을 가져온다. 
                    temp.left = node.left # 가장 작은 노드를 가져와서 노드로 올리기 위해 왼쪽 자식을 업데이트 
                    if parent != node: # parent의 왼쪽 자식이 위로 올라가므로 parent의 왼쪽 자식의 오른쪽 노드를 왼쪽 노드로 업데이트 
                        parent.left = temp.right
                        temp.right = node.right 
                    node = temp 
                    return node, True 
        elif data < node.data:
            node.left, is_deleted = self.delete_value(node.left, data) # 데이터가 작으면 왼쪽으로 이동 
        else:
            node.right, is_deleted = self.delete_value(node.right, data) # 데이터가 크면 오른쪽으로 이동 
        return node.data, is_deleted

array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]
bst = BinarySearchTree()
for x in array:
    bst.insert(x)

print(bst.find(4))
print(bst.find(50))

print(bst.delete(15))
            





# 테스트케이스 6,7번이 런타임 에러가 발생 
# 알고보니 재귀 횟수 제한때문이다!
# 재귀를 쓸 때 sys.setrecursionlimit 설정 꼭꼭하자 
import sys

class Node:
    def __init__(self, value, x, y):
        self.x = x
        self.y = y
        self.value = value
        self.left = None
        self.right = None
        
def insert(node, value, x, y):
    if node.x < x and node.y > y:
        if node.right == None:
            new_node = Node(value, x, y)
            node.right = new_node
        else:
            insert(node.right, value, x, y)
    elif node.x > x and node.y > y:
        if node.left == None:
            new_node = Node(value, x, y)
            node.left = new_node
        else:
            insert(node.left, value, x, y)
        
    
def solution(nodeinfo):
    sys.setrecursionlimit(10**7)
    answer = []
    # if len(nodeinfo) == 1:
    #     answer.append([1])
    #     answer.append([1])
    #     return 
    
    temp = sorted(nodeinfo, key = lambda x: (-x[1])) # y를 기준으로 정렬해서 root를 찾는다. 
    root_index = nodeinfo.index(temp[0])
    root = Node(root_index + 1, nodeinfo[root_index][0], nodeinfo[root_index][1])
    
    temp = temp[1:]
    
    while temp:
        node = temp.pop(0)
        index = nodeinfo.index(node)
        insert(root, index + 1, node[0], node[1])
    
    pre = []
    post = []
    
    def preorder(node): # 전위 순회 
        pre.append(node.value)
        if node.left != None:
            preorder(node.left)
        if node.right != None:    
            preorder(node.right)
            
    def postorder(node): # 후위 순회 
        if node.left != None:
            postorder(node.left)
        if node.right != None:
            postorder(node.right)
        post.append(node.value)
            
    preorder(root)
    postorder(root)
    
    answer.append(pre)
    answer.append(post)
    return answer
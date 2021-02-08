# 이진탐색 트리 
# 정해진 갯수없이 무한으로 입력받는 방법!!! 

# 시간초과 
# 코드도 더럽고 일단 시간초과가 발생해서 그런 것 같아서 코드를 좀 정리해보자 -> 5639_BST1.py


import sys
input = sys.stdin.readline

# node 클래스를 생성 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def main():
    sys.setrecursionlimit(10 ** 7)
    vertex = [0]
    while True:
        try:
            v = int(input())
            vertex.append(v)
        except:
            break 

    n = len(vertex)

    for i in range(1, n): # 전위 순회 결과를 통해서 트리 다시 만들기 
        if i == 1:
            new_node = Node(vertex[i])
            root = new_node
        else:
            if root.data > vertex[i]: # 루트 왼쪽 
                parent = root 
                node = root.left 
                while node:
                    parent = node 
                    if parent.data > vertex[i]:
                        node = node.left 
                    else:
                        node = node.right 
                if parent.data < vertex[i]: # 부모보다 크면 오른쪽 
                    new_node = Node(vertex[i])
                    parent.right = new_node
                else: # 부모보다 작으면 왼쪽 
                    new_node = Node(vertex[i])
                    parent.left = new_node
            else: # 루트 오른쪽 
                parent = root
                node = root.right 
                while node:
                    parent = node 
                    if parent.data > vertex[i]: # 부모보다 데이터가 작으면 왼쪽으로 
                        node = node.left 
                    else: # 부모보다 데이터가 크면 오른쪽으로 
                        node = node.right 
                if parent.data < vertex[i]: # 부모보다 크면 오른쪽 
                    new_node = Node(vertex[i])
                    parent.right = new_node
                else: # 부모보다 작으면 왼쪽 
                    new_node = Node(vertex[i])
                    parent.left = new_node
    

    def postorder_traverse(node): # 후위 순회 -> 완쪽 오른쪽 루트 
        if node:
            # if node.left: # 왼쪽 자식이 있는 경우 
            #     postorder_traverse(node.left)
            #     postorder_traverse(node.right)
            #     print(node.data) # 루트 출력 
            # else:
            #     print(node.data)
            postorder_traverse(node.left)
            postorder_traverse(node.right)
            print(node.data)
            
    postorder_traverse(root)
    
    # print()
    # print()

    # def preorder_traverse(node): # 전위 순회 -> 루트 왼쪽 오른쪽 
    #     if node:
    #         print(node.data)
    #         preorder_traverse(node.left)
    #         preorder_traverse(node.right)
    
    # preorder_traverse(root)


    #print(vertex)

if __name__ ==  "__main__":
    main()

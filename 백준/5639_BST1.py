# 이진탐색 트리 
# 정해진 갯수없이 무한으로 입력받는 방법!!! 

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
    vertex = []
    while True:
        try:
            v = int(input())
            vertex.append(v)
        except:
            break 

    n = len(vertex)
    
    for i in range(n): # 전위 순회 결과를 통해서 트리 다시 만들기 
        if i == 0:
            root = Node(vertex[i])
        else:
            node = root 
            while node:
                parent = node 
                if node.data < vertex[i]:
                    node = node.right 
                else:
                    node = node.left 
            if parent.data < vertex[i]:
                parent.right = Node(vertex[i])
            else:
                parent.left = Node(vertex[i])

            #print(parent.data, vertex[i])
    

    def postorder_traverse(node): # 후위 순회 -> 완쪽 오른쪽 루트 
        if node:
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

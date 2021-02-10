# 이진탐색 트리 
# 정해진 갯수없이 무한으로 입력받는 방법!!! 


# 내가 한 방식은 전위순회 결과로 먼저 BST를 만들고 그 만든 BST를 이용해서 후위순회 하는 것을 구현함
# 근데 이렇게하면 문제에서 주어진 시간 안에 풀지 못해 시간초과가 발생한다.
 
## 그래서 분할 정복을 이용한다. (전위 순회의 장점은 전위 순회 결과를 이용해서 트리를 다시 만들 수 있다는 것!) --> 5639_BST2.py
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

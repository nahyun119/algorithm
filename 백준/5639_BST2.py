# 분할정복을 이용해서 풀어보자 

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


    def postorder_traverse(start, end):
        if start > end:
            return 
        node = vertex[start] # -> root 
        boundary = end + 1
        for i in range(start + 1, end + 1):
            if node < vertex[i]:
                boundary = i # 나눌 경계값 
                break
    

        postorder_traverse(start + 1, boundary - 1)
        postorder_traverse(boundary, end)
        print(node)


    postorder_traverse(0, n - 1)

if __name__ ==  "__main__":
    main()

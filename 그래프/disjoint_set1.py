# disjoint set의 연산인 union, find 연산을 이용해서 
# 무방향 그래프에서 cycle 여부를 판단하는 코드 

import sys


def find_parent(parent, x):
    if parent[x] != x: # 루트 노드가 아닌 경우
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a 
    else:
        parent[a] = b 

def main():

    sys.setrecursionlimit(10000)

    v, e = map(int, input().split())
    parent = [0] * (v + 1)

    for i in range(1, v + 1):
        parent[i] = i
    
    cycle = False

    for i in range(e):
        a, b = map(int, input().split())

        if find_parent(parent, a) == find_parent(parent, b): # 간선을 이루는 두 노드의 루트 노드가 동일하다면 cycle이 발생
            cycle = True
            break
        else:
            union_parent(parent, a, b) # 두 노드의 루트 노드가 다르다면 union 연산을 진행 


    if cycle:
        print("cycle이 발생")
    else:
        print("cycle이 발생하지 않음")


if __name__ ==  "__main__":
    main() 
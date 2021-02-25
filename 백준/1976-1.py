# 1976번을 union find로 푼다 

# 플로이드로 풀면 2508ms 가 걸린다. 원래 O(N ^ 3)이므로 
# 근데 union find를 사용하면 72ms 엄청 간단해진다. 

import sys

input = sys.stdin.readline

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union_parent(a, b, parent):
    pa = find_parent(a, parent)
    pb = find_parent(b, parent)

    if pa < pb :
        parent[pb] = pa
    else:
        parent[pa] = pb


def main():
    n = int(input())
    m = int(input())

    graph = [] # 간선 정보 
    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(n):
            if temp[j] == 1:
                graph.append((i + 1, j + 1))
        #graph.append((i, i))
    citys = list(map(int, input().split()))
    parent = [] # 부모를 자기 자신으로 초기화 
    for i in range(n + 1): # 1부터 시작 
        parent.append(i)
    

    for x, y in graph:
        if find_parent(x, parent) != find_parent(y, parent): # 부모가 다르면 잇는다. 
            union_parent(x, y, parent)
    
    for i in range(m - 1):
        if parent[citys[i]] != parent[citys[i + 1]]: # 부모가 다르다면 이어져 있지 않다. 
            print("NO")
            return

    print("YES")



if __name__ ==  "__main__":
    main()
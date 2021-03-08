# 모든 섬을 연결하고 사이클이 없고 
# 비용이 최소 -> minimum spanning tree -> kruskal

# 테스트케이스랑 결과가 안맞아서 뭔가했는데,, 거리를 구할 때 거리 제곱에 e를 계속 곱해야한다. 이게 cost 
# 한번에 계산하는 것이 아니다 ! 

import math 

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(a, b, parent):
    pa = find_parent(parent, a)
    pb = find_parent(parent, b)

    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb
 

def solve():
    n = int(input())

    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())
    
    result = 0

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            # cost = abs(x[i] - x[j]) + abs(y[i] - y[j])
            cost = math.sqrt((x[i] - x[j])** 2 + (y[j] - y[i]) ** 2) ** 2 * e
            edges.append((cost, i, j))
            #edges.append((cost, j ,i))

    #print(edges)
    edges.sort()

    parent = [x for x in range(n)]
    
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) == find_parent(parent, b):
            continue
        else:
            union_parent(a, b, parent)
            result += cost 
            
    
    return round(result)




def main():
    T = int(input())
    for i in range(T):
        result = solve()
        print("#" + str(i + 1), result)

if __name__ ==  "__main__":
    main()

# 터널 즉, 간선의 수가 도시 수 - 1이므로 트리임을 짐작할 수 있다. 
# 그리고 터널 건설 비용이 최소 비용이 되고 모든 도사를 연결할 수 있도록 하므로 
# 이 문제 또한 최소 신장 트리 문제로 kruskal 알고리즘을 이용하는 것을 짐작할 수 있다.
import sys
input = sys.stdin.readline # 그냥 input 사용했는데 시간 초과나서 더 빠른 sys.stdin.readline 이용 

def find_parent(parent, x):
    if parent[x] != x:
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
    n = int(input())
    planet_x = [] # 행성 정보
    planet_y = []
    planet_z = [] 
    parent = [0] * (n + 1)

    edges = []
    
    for i in range(1, n + 1):
        x, y, z = map(int, input().split())
        planet_x.append((x, i))
        planet_y.append((y, i))
        planet_z.append((z, i))

    # x, y, z에 대해서 각각 정렬한 후 간선의 수 n - 1개만큼 간선을 저장할 수 있다. 
    planet_x.sort()
    planet_y.sort()
    planet_z.sort()
    
    for i in range(n - 1):
        edges.append((planet_x[i+1][0] - planet_x[i][0], planet_x[i][1], planet_x[i + 1][1]))
        edges.append((planet_y[i+1][0] - planet_y[i][0], planet_y[i][1], planet_y[i + 1][1]))
        edges.append((planet_z[i+1][0] - planet_z[i][0], planet_z[i][1], planet_z[i + 1][1]))


    # 행성 사이 거리를 이용해서 터널 비용 구하기 -> 이렇게 하면 간선의 수 n * (n - 1) /2 가 되는데 그러면 간선의 수가 너무 많아서 메모리 초과 발생 
    for i in range(1, n + 1):
        # x1, y1, z1 = planet[i]
        # for j in range(i + 1, n): 
        #     x2, y2, z2 = planet[j]  
        #     cost = min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
        #     edges.append((cost, i, j))
        parent[i] = i # 부모 테이블 초기화  

    edges.sort() # 꼭 정렬해라,,,,
    #print(edges)
    result = 0
    for edge in edges:
        cost, x, y = edge  
        if find_parent(parent, x) != find_parent(parent, y): # 사이클이 아닌 경우
            union_parent(parent, x, y)
            result += cost
    
    print(result)




if __name__ ==  "__main__":
    main()
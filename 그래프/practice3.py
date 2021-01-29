# 거리마다 비용이 있고, 비용을 최소로 하며 도시들이 연결되어야하므로
# 최소 신장 트리를 구하는 kruskal 알고리즘 사용 

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
    n, m = map(int, input().split())

    edges = []
    total_cost = 0 # 모든 도로 길이 
    for _ in range(m): # 도로 수만큼 
        x, y, z = map(int, input().split())
        total_cost += z
        edges.append((z, x, y))

    parent = [0] * n
    for i in range(n):
        parent[i] = i

    edges.sort() # 오름차순 정렬

    result = 0 

    for edge in edges:
        cost, x, y = edge
        if find_parent(parent, x) != find_parent(parent, y): # cycle이 발생하지 않으면 
            union_parent(parent, x, y)
            result += cost 
    
    print(total_cost - result)
            



if __name__ ==  "__main__":
    main()
# 최소 스패닝 트리 -> kruskal 알고리즘 
import heapq

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(a, b, parent):
    pa = find_parent(parent, a)
    pb = find_parent(parent, b)

    if pa < pb:
        parent[pb] = pa 
    else:
        parent[pa] = pb

v, e = map(int, input().split())
edges = []
for i in range(e):
    a,b,c = map(int, input().split())
    heapq.heappush(edges, (c, a, b))

parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

result = 0
while edges:
    cost, a, b = heapq.heappop(edges)
    
    if find_parent(parent, a) == find_parent(parent, b):
        continue 
    else:
        union_parent(a, b, parent)
        result += cost 
print(result)


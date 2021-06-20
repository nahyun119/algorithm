import sys 
import heapq 
input = sys.stdin.readline 

v, e = map(int, input().split())

graph = []

for i in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(graph, (c, a, b))

# 최소 가중치 순서대로 진행해야하므로 가중치 기준으로 정렬 
# graph.sort(key = lambda x : x[2])

## 나는 정렬을 이용해서 문제를 풀었지만, 정렬이 아니라 heapq를 이용해서도 문제를 풀 수 있다!!! heapq에서 맨처음 인자를 기준으로 알아서 정렬이 이루어지기 때문 


def find_parent(x, parent): # 해당 정점의 부모 찾기 
    if parent[x] != x: # 부모가 다르다면
        parent[x] = find_parent(parent[x], parent) # 부모 계속 찾아서 업데이트 할 수 있도록 
    return parent[x]

def union_parent(a, b, parent): # 정점을 연결하기 위해 해당 정점의 부모들을 찾아서 연결하도록 부모 업데이트 
    pa = find_parent(a, parent)
    pb = find_parent(b, parent)

    if pa > pb: # 정점 번호가 더 작은게 부모가 된다 
        parent[pa] = pb 
    elif pa < pb:
        parent[pb] = pa 
    
total = 0
parent = [x for x in range(v + 1)] # 부모 정보 

# for x, y, cost in graph:
#     if find_parent(x, parent) == find_parent(y, parent): # 부모가 동일하다면 사이클이 생기는 간선이라면 넘어간다 
#         continue
#     else:
#         union_parent(x, y, parent)
#         total += cost 

while graph:
    cost, x, y = heapq.heappop(graph)

    if find_parent(x, parent) == find_parent(y, parent):
        continue 
    else:
        union_parent(x, y, parent)
        total += cost 
# print(parent)
print(total)   
    
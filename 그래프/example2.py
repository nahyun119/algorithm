# 마을의 모든 집들이 서로 갈 수 있고, 길을 없앤 후에도 조건을 유지하고 
# 길의 유지비를 최소로 할 수 있도록 길을 제거
# -> 최소 신장 트리 문제 kruskal algorithm을 이용
# 2개의 최소 신장 트리를 만들어야 한다. 

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x]) # n도 100000, m은 1000000이므로 경로 압축 이용 
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

    parent = [0] * (n + 1) # 1번부터 n까지 시작하므로 
    for i in range(1, n + 1):
        parent[i] = i # parent 초기화

    edges = []

    for i in range(m):
        a, b, c = map(int, input().split())
        edges.append((c, a, b)) # a에서 b로 가는데 c 
    
    edges.sort() # 오름차순 정렬

    result = 0 # 비용 
    max_cost = -1
    
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) == find_parent(parent, b): # 루트가 같으면 cycle이므로 패스
            continue
        else:
            union_parent(parent, a, b) # a랑 b랑 합치기
            if max_cost < cost: # 사실 cost 기준으로 오름차순 정렬이 이미 되어있어서 그냥 마지막에 넣는 cost가 최대이긴 하다. 
                max_cost = cost
                max_edge = (a, b)
            result += cost

    print(max_cost, max_edge) 
    print(result - max_cost) # 최소 신장 트리를 이루는 간선 중 비용이 제일 비싼 간선을 제거해서 최소 신장 트리 2개를 만든다. 


    


if __name__ ==  "__main__":
    main()
# 최소 신장 트리 알고리즘인 kruskal 알고리즘 

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x]) # 루트 노드가 아닌 경우, 부모 노드를 통해 재귀적으로 이동 
    return parent[x] 

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    

def main():
    v, e = map(int, input().split())
    parent = [0] * (v + 1)

    edges = [] # 간선을 담을 리스트
    result = 0 # 최소 신장 비용 

    for i in range(1, v + 1):
        parent[i] = i # 부모 테이블 초기화 
    
    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))
    
    edges.sort() # 비용을 기준으로 오름차순 정렬

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) == find_parent(parent, b): # 두 노드의 루트 노드가 동일하다면, 즉 cycle 발생
            continue
        else: # cycle 발생 아니라면 
            union_parent(parent, a, b) # union 진행 
            result += cost # 비용 계산 
    
    print(result)



if __name__ ==  "__main__":
    main()

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

    graph = []  # n x n 행렬
    for i in range(n):
        graph.append(list(map(int, input().split())))

    parent = [0] *  n

    for i in range(n):
        parent[i] = i # 부모 초기화 
    
    # print(graph)
    # print(parent)

    for i in range(n):
        for j in range(n):
            if i < j: # 양방향이라서 그냥 간선 하나만 확인하도록 
                if graph[i][j] == 1: # 연결되면 
                    union_parent(parent, i, j)
                    #print(parent)
    
    citys = list(map(int, input().split()))
    is_possible = True

    # 내가 한 방법, 경로 압축을 이용하면 결과적으로 나오는 parent 테이블은 해당 노드의 루트 노드로 되므로 
    root = parent[citys[0] - 1] # 0 ~ n- 1로 진행했으므로 결과 노드도 -1해서 진행하도록 
    for city in citys:
        if parent[city - 1] != root:
            is_possible = False
    
    # 아니면 find_parent해서 루트 노드 찾아서 진행하는것도 나쁘지 않다. 
    for i in range(m - 1):
        if find_parent(parent, citys[i] - 1) != find_parent(parent, citys[i + 1]  - 1):
            is_possible = False 
    
    if not is_possible:
        print("NO")
    else:
        print("YES")


    #print(parent)




if __name__ ==  "__main__":
    main()
INF = 1e9
def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union_parent(a, b, parent):
    pa = find_parent(a, parent)
    pb = find_parent(b, parent)

    if pa < pb:
        parent[pb] = pa 
    else:
        parent[pa] = pb

def solve(n):
    graph = list(map(int, input().split()))
    
    edges = []
    for i in range(0, n * 2, 2):
        edges.append((graph[i], graph[i + 1]))
    
    parent = []

    for i in range(100):
        parent.append(i)

    for e in edges:
        if find_parent(e[0], parent) != find_parent(e[1], parent):
            union_parent(e[0], e[1], parent)
        else:
            continue
            
    if parent[0] == parent[99]:
        return 1
    else:
        return 0


def main():
    for _ in range(10):
        a, b = map(int, input().split())
        result = solve(b)
        print("#" + str(a), result)

if __name__ ==  "__main__":
    main()
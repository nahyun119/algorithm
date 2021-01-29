def find_parent(parent, x):
    if parent[x] != x: # 루트 노드가 아닌 경우 
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a # b를 a에 연결 
    else:
        parent[a] = b # a를 b에 연결 


def main():
    n, m = map(int, input().split())

    parent = [0] * (n + 1)
    result = []
    for i in range(n + 1):
        parent[i] = i # 자기 자신으로 업데이트 

    for i in range(m):
        op, a, b = map(int, input().split())
        if op == 0 : # 0이면 union
            union_parent(parent, a, b)
        if op == 1: # 1이면 find
            pa = find_parent(parent, a)
            pb = find_parent(parent, b) 
            if pa == pb: # 루트 노드가 동일하면 같은 팀, 같은 집합
                result.append("YES")
            else:
                result.append("NO")
        
    for i in result:
        print(i)


if __name__ ==  "__main__":
    main()
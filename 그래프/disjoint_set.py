# 서로소 집합의 기본 연산(find, union) 알고리즘

# 해당 노드 x의 부모 노드를 찾는 함수 

# 이렇게 재귀적으로 그냥 호출하게 되면 최악의 경우 모든 노드를 탐색해야하므로 O(V) 만큼 소요된다.
# 이렇게하면 전체적으로 O(VM)만큼 (노드 수 * 연산 수) 걸리므로 비효율적 
# 따라서 부모를 찾는 함수를 재귀적으로 호출할 때마다 부모 테이블을 갱신하는 방법을 이용해서 보다 효율적으로 구현할 수 있다. 

def find_parent(parent, x):

    if parent[x] != x: # 루트 노드가 아닌 경우(자기 자신과 부모 노드가 동일하지 않은 경우)
        return find_parent(parent, parent[x]) # 부모를 이용해서 재귀적으로 루트노드를 찾도록 
    return x # 루트 노드인 경우 

def better_find_parent(parent, x):
    if parent[x] != x:
        parent[x] = better_find_parent(parent, parent[x]) # 재귀적으로 호출할 때마다 그 값을 부모테이블에 저장하고 부모를 return 
        # 이렇게하면 루트 노드에 보다 빠르게 접근할 수 있다. 부모 테이블이 루트 노드 정보로 업데이트되므로 
    return parent[x]

# 두 원소가 속한 집합을 합치는 함수 
def union_parent(parent, a, b):
    # a = find_parent(parent, a)
    # b = find_parent(parent, b)

    a = better_find_parent(parent, a)
    b = better_find_parent(parent, b)

    if a < b:
        parent[b] = a # a가 노드번호가 작으면 b가 a를 가리키도록 
    else:
        parent[a] = b # b가 노드번호가 작으면 a가 b를 가리키도록 

def main():
    v, e = map(int, input().split()) # 노드 갯수와 간선 갯수(union 연산 수)

    parent = [0] * (v + 1) # 1번부터 시작하므로 

    for i in range(1, v + 1):
        parent[i] = i # 맨처음 부모노드를 자기 자신으로 초기화 
    
    for i in range(e):
        a, b = map(int, input().split())
        union_parent(parent, a, b)
    
    for i in range(1, v + 1): # 각 원소가 속한 집합의 루트노드 출력 
        print(better_find_parent(parent, i), end = ' ')
    
    print()

    for i in range(1, v + 1):
        print(parent[i], end = ' ') # 부모테이블 출력 



if __name__ ==  "__main__":
    main()    
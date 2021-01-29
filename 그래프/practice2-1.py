# 그래프의 서로소 집합 연산을 이용해서 풀이
# 도킹하는 과정을 합집합 연산으로 이해하고, 해당 비행기의 root가 0이 아니라면 왼쪽 노드와 합집합 연산을 진행한다. 

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
    g = int(input()) # 탑승구 수 
    p = int(input()) # 비행기 수 

    parent = [0] * (g + 1) # 부모 테이블 초기화

    for i in range(1, g + 1):
        parent[i] = i  # 자기 자신으로 초기화 

    count = 0
    is_done = False 
    for i in range(p):
        airplane = int(input())

        root_a = find_parent(parent, airplane)
        if root_a != 0: # 0이 아니라면 도킹 가능 
            # 루트랑 루트 왼쪽 노드와 합집합 연산
            union_parent(parent, root_a, root_a - 1)
            if not is_done:
                count += 1
        else:
            is_done = True

        #print(parent)

    print(count)

if __name__ ==  "__main__":
    main()
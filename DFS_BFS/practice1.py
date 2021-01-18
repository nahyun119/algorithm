from collections import deque

def main():
    N, M, K, X = map(int, input().split())
    graph = [[] for _ in range(N)]

    for value in range(M):
        x, y = map(int, input().split())
        graph[x - 1].append(y - 1) # 단방향 도로 
    
    cost = [-1] * N
    cost[X - 1] = 0
    queue = deque()
    queue.append(X - 1)
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if cost[i] == 0:
                cost[i] = cost[node] + 1
                queue.append(i)
    
    check = False
    for i in range(N):
        if cost[i] == K:
            print(i + 1)
            check = True

    if not check:
        print(-1)   


if __name__ ==  "__main__":
    main()
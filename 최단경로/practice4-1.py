# 헛간 사이의 모든 거리가 동일하므로 bfs를 이용해서 각각 경로를 구할 수 있다.
# bfs를 이용해서 문제를 풀어보자

from collections import deque

def main():
    n, m = map(int, input().split())
    
    graph = [[] for _ in range(n + 1)] # 갈 수 있다는걸 표현하기 위해서 이차원 리스트로 

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a) # 양방향 
    
    visited = [0] * (n + 1)
    visited[0] = 1 # 0번은 갈 수 없으므로 미리 방문 표시 
    visited[1] = 1

    queue = deque()
    queue.append((1, 0)) # 1번 노드부터 시작, 거리 0

    distance = [0] * (n + 1)


    while queue:
        node, cost = queue.popleft()
        for x in graph[node]:
            #print(x)
            if visited[x] == 0: # 방문 안한 경우 
                queue.append((x, cost + 1)) # 이전 노드 방문한 cost + 1로 업데이트 
                distance[x] = cost + 1
                visited[x] = 1

    max_value = max(distance)

    print(distance.index(max_value), max_value, distance.count(max_value))


if __name__ ==  "__main__":
    main()

import sys
from collections import deque

input = sys.stdin.readline


def main():
    n, m, v = map(int, input().split())

    graph = [[0] * (n + 1) for _ in range(n + 1)] # 1~n까지이므로

    for _ in range(m):
        a, b = map(int, input().split()) # 간선은 양방향
        graph[a][b] = 1
        graph[b][a] = 1
    
    
    d_visited = [0] * (n + 1)
    #dfs_result = []

    def dfs(start, d_visited):
        print(start, end = ' ')
        #dfs_result.append(start)
        d_visited[start] = 1
        for i in range(1, n + 1):
            if graph[start][i] == 1 and d_visited[i] == 0: # 자기 자신이 아닌 경우 
                dfs(i, d_visited)

    dfs(v, d_visited)
    
    print() 

    q = deque()
    q.append(v)
    b_visited = [0] * (n + 1) # bfs 방문 
    b_visited[v] = 1
    # bfs_result = []

    while q:
        node = q.popleft()
        print(node, end = ' ')

        for i in range(1, n + 1):
            if graph[node][i] == 1 and b_visited[i] == 0:
                q.append(i)
                b_visited[i] = 1 ## visited 여기서 진행!!!!!!!!!!!
    
    # print(*dfs_result)
    # print(*bfs_result) #  - > 이런식으로 *을하면 [1, 2, 4, 3]이 1 2 4 3 이렇게 나옴 ;;


if __name__ ==  "__main__":
    main()
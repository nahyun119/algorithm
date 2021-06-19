import sys 
input = sys.stdin.readline

n = int(input())

graph = [[] for i in range(n)]
for i in range(n):
    t = list(input().strip())
    graph[i] = [int(x) for x in t]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * n for _ in range(n)]

def dfs(x, y):
    visited[x][y] = 1
    count = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0: # 방문 안한 경우 
                if graph[nx][ny] == 1: # 이동할 수 있는 경우 
                    count += dfs(nx, ny) # 거리를 계속 더해서 이동하도록 1에서부터 return 되면서 차례대로 거리가 더해진다.
    # print(x, y, count)
    return count 

result = 0
result_list = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 1:
            count = dfs(i, j)
            result += 1
            result_list.append(count)
    
result_list.sort()
print(result)
for i in result_list:
    print(i) 
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline 

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input().strip()))

visited = [[0] * n for _ in range(n)]
visited2 = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs2(x, y):
    
    visited2[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if visited2[nx][ny] == 0:
                if graph[x][y] == 'B':
                    if graph[nx][ny] == graph[x][y]:
                        dfs2(nx, ny)
                else:
                    if graph[nx][ny] != 'B':
                        dfs2(nx, ny)

def dfs(x, y):
    
    visited[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if visited[nx][ny] == 0 and graph[nx][ny] == graph[x][y]:
                dfs(nx, ny)

count1 = 0 
count2 = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            count1 += 1
        if visited2[i][j] == 0:
            dfs2(i, j)
            count2 += 1
             
print(count1, count2)

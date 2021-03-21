import sys
input = sys.stdin.readline
r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(lambda x : ord(x) - 65, input().strip())))



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_value = 0

visited = [0] * 26
visited[graph[0][0]] = 1

def dfs(x, y, length):
    global max_value 
    
    max_value = max(max_value, length)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < r and ny >= 0 and ny < c:
            if visited[graph[nx][ny]] == 0:
                visited[graph[nx][ny]] = 1
                dfs(nx, ny, length + 1)
                visited[graph[nx][ny]] = 0 

dfs(0, 0, 1)
print(max_value)

    


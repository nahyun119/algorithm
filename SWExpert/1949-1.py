# dfs, 백트래킹을 이용한 문제
T = int(input())

def dfs(x, y, count, k, n):
    global result
    
    result = max(count, result)

    #print(result)

    visited[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if visited[nx][ny] == 0:
                if graph[nx][ny] < graph[x][y]:
                    dfs(nx, ny, count + 1, k, n)
                else:
                    # 최대 k만큼 뺐을 때 graph보다 작아지는 경우 graph[x][y]에서 이동하기 위해 graph[nx][ny] = graph[x][y] - 1 로 업데이트
                    if graph[nx][ny] - k < graph[x][y]:
                        pre = graph[nx][ny]
                        graph[nx][ny] = graph[x][y] - 1
                        dfs(nx, ny, count + 1, 0, n)
                        graph[nx][ny] = pre
                        

    visited[x][y] = 0
        

for t in range(T):
    n, k = map(int, input().split())
    graph = []
    start = []
    max_value = 0
    result = 0
    for j in range(n):
        temp = list(map(int, input().split()))
        v = max(temp)
        if max_value < v:
            start = []
            for i in range(n):
                if temp[i] == v:
                    start.append((j , i))
            max_value = v
        elif max_value == v:
            for i in range(n):
                if temp[i] == v:
                    start.append((j , i))
        graph.append(temp)

    visited = [[0] * n for _ in range(n)]

    for x, y in start:
        dfs(x, y, 1, k, n)
    
    print("#" + str(t + 1), result)

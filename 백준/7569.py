# 7576을 3차원으로 확장한 문제 

from collections import deque


def main():
    m, n, h = map(int, input().split())
    
    graph = []

    for i in range(h):
        box = []
        for j in range(n):
            box.append(list(map(int, input().split())))
        graph.append(box)

    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1] # 3차원이므로 z축 추가 

    q = deque()
    visited = [[[0] * m for _ in range(n)] for _ in range(h)]

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    q.append((j, k, i, 0)) # x, y, z, 비용 

    total_day = 0


    while q:
        x, y, z, day = q.popleft()
        if total_day < day:
            total_day = day
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m and nz >= 0 and nz < h:
                if graph[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = 1
                    q.append((nx, ny, nz, day + 1))
                    visited[nz][nx][ny] = 1

    
    for i in range(h):
        for j in range(n):
            if 0 in graph[i][j]: # 하나라도 익지 않은 경우 
                print(-1) 
                return 

    print(total_day)



if __name__ ==  "__main__":
    main()
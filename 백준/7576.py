# 모든 토마토들이 익는 최소 날짜를 구하는 것이기 때문에 
# bfs 
from collections import deque

def main():
    m, n = map(int, input().split()) # n이 행, m이 열 

    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 토마토 시작 위치 찾기 
   
    q = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((i, j, 0)) # 토마토가 하나 이상이기 때문에 1인 애는 먼저 넣어놓는다. 

    visited = [[0] * m for _ in range(n)] # 방문

    #q.append((x, y, 0)) # 좌표랑 시간 
    total_day = 0
    while q:
        x, y, day = q.popleft()
        #print(visited)
        if total_day < day:
            total_day = day
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    graph[nx][ny] = 1 # 오염으로 변경 
                    q.append((nx, ny, day + 1))
                    visited[nx][ny] = 1

    for i in range(n):
        if 0 in graph[i]: # 토마토가 하나라도 익지 못하는 상황이면 
            print(-1)
            return 
        
    print(total_day)
    #print(graph)

    #print(x, y)
    
    


if __name__ ==  "__main__":
    main()
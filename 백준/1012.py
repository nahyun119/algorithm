# 2667번과 매우 유사한 문제

import sys


result = []

def search():
    global result 
    m, n, k = map(int, input().split()) # 가로, 세로, 심어져있는 배추 수

    graph = [[0] * n for _ in range(m)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    
    visited = [[0] * n for _ in range(m)]

    def dfs(x, y, visited):
        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    dfs(nx, ny, visited)
             
    count = 0

    for i in range(m): # 가로 
        for j in range(n): # 세로 
            if graph[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j, visited)
                count += 1

    #print(count)
    result.append(count)


def main():
    sys.setrecursionlimit(10**7)
    
    global result 
    T = int(input())

    for i in range(T):
        search()
    
    for i in range(T):
        print(result[i])

if __name__ ==  "__main__":
    main()
# 무리를 지으는 것이므로 
# 탐색하면서 1이고 방문 안한 경우 거기서부터 dfs를 진행해서
# 상하좌우로 연결된 애들 중 1인 애들에게 이동하면서 무리를 만들도록 

import sys

def main():
    sys.setrecursionlimit(10**7)
    n = int(input())
    graph = []

    for _ in range(n):
        row = list(str(input()))
        graph.append(row)
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1] # 상하좌우 이동
    
    visited = [[0] * n for _ in range(n)]

    # print(graph)
    # print(visited)

    def dfs(x, y, visited, number):
        visited[x][y] = number
        #print(x, y, visited)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if graph[nx][ny] == '1' and visited[nx][ny] == 0:
                    dfs(nx, ny, visited, number)

    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '1' and visited[i][j] == 0:
                # print(i, j)
                count += 1
                dfs(i, j, visited, count)
                

    print(count)
    result = []
    for i in range(1, count + 1):
        total = 0
        for j in range(n):
            total += visited[j].count(i)
        result.append(total)

    result.sort()
    for i in range(count):
        print(result[i])
    
        
            


if __name__ ==  "__main__":
    main()
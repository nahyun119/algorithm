import sys
from collections import deque
input = sys.stdin.readline

def main():
    m, n, k = map(int, input().split())

    graph = [[0] * n for _ in range(m)]

    for _ in range(k):
        lx, ly, rx, ry = map(int, input().split())
        for i in range(ly, ry):
            for j in range(lx, rx):
                graph[i][j] = 1
    visited = [[0] * n for _ in range(m)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    result = []
    # def dfs(x, y, visited, step, count):
    #     #print(x, y, step, count)
    #     visited[x][y] = 1

    #     if result[step] < count:
    #         result[step] = count

    #     for i in range(4):
    #         nx = x + dx[i]
    #         ny = y + dy[i]

    #         if nx >= 0 and nx < m and ny >= 0 and ny < n:
    #             if graph[nx][ny] == 0 and visited[nx][ny] == 0:
    #                 count += 1
    #                 dfs(nx, ny, visited, step, count)
    q = deque()

    def bfs():
        count = 0

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and nx < m and ny >= 0 and ny < n:
                    if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                        q.append((nx, ny))
                        visited[nx][ny] = 1
            count += 1
        if count == 1:
            return count 

        return count - 1

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 0 and visited[i][j] == 0:
                # result.append(0)
                # dfs(i, j, visited, count, 0)
                # count += 1
                q.append((i, j))
                c = bfs()
                result.append(c)


    result.sort()
    print(len(result))
    print(*result)

if __name__ ==  "__main__":
    main()
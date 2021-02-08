# dfs 이용 한 곳에서 이동할 수 있는 곳을 확인하기 때문에 

import sys
input = sys.stdin.readline

def main():
    sys.setrecursionlimit(10 ** 7)
    result = []
    w, h = map(int, input().split())

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]


    def dfs(x, y, graph, visited):
        visited[x][y] = 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < h and ny >= 0 and ny < w:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    dfs(nx, ny, graph, visited)


    while w != 0 and h != 0:
        count = 0
        graph = []
        for i in range(h):
            graph.append(list(map(int, input().split())))
        
        visited = [[0] * w for _ in range(h)]

        if w == 1 and h == 1:
            if graph[0][0] == 0:
                result.append(0)
            else:
                result.append(1)
        else:
            for i in range(h):
                for j in range(w):
                    if graph[i][j] == 1 and visited[i][j] == 0:
                        dfs(i, j, graph, visited)
                        count += 1
        
            result.append(count)
        w, h = map(int, input().split())

    #print(result)

    for r in result:
        print(r)

if __name__ ==  "__main__":
    main()
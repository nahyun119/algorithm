import sys
from itertools import chain, repeat
input = sys.stdin.readline

def main():
    sys.setrecursionlimit(10 ** 7)
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    temp = list(chain.from_iterable(graph))
    
    min_value = min(temp)
    max_value = max(temp)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    def dfs(x, y, visited, value):
        visited[x][y] = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if graph[nx][ny] > value and visited[nx][ny] == 0:
                    dfs(nx, ny, visited, value)
        
    result = []

    
    for i in range(min_value, max_value): # max이상이면 안전한 영역이 없으므로 제외
        visited = [[0] * n for _ in range(n)]
        count = 0
        for a in range(n):
            for b in range(n):
                if graph[a][b] > i and visited[a][b] == 0:
                    dfs(a, b, visited, i)
                    count += 1
        result.append(count)
    if result:
        print(max(result))
    else:
        print(1) # 물에 잠기지 않는 경우 

if __name__ ==  "__main__":
    main()
from collections import deque

def main():
    N, M = map(int, input().split())

    graph = []
    for value in range(N):
        graph.append(list(map(int, input())))
    
    queue = deque()
    #visited = [[0] * M for _ in range(N)]

    queue.append((0,0))


    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    while queue:
        node = queue.popleft()

        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[node[0]][node[1]] + 1
                queue.append((nx, ny))
            if graph[nx][ny] == 0:
                continue

    print(graph[N-1][M-1])
            


if __name__ ==  "__main__":
    main()

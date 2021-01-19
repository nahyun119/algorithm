# 통과는 했지만 이미 queue에 들어가서 나온 데이터는 이미 상하좌우로 이동했으므로
# 이동할 수 없기 때문에 굳이 queue에 다시 넣을 필요가 없다.
# 그냥 이동해서 나온 애들만 넣으면 될 것 같다. -> practice3-1.py

from collections import deque
import sys
def main():
    N, K = map(int, sys.stdin.readline().rstrip().split())
    graph = []

    for value in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

    S, X, Y = map(int, sys.stdin.readline().rstrip().split())

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    count = 0

    def add_quque():
        for value in range(1, K + 1):
            for i in range(N):
                for j in range(N):
                    if graph[i][j] == value:
                        queue.append((i, j))

    while count < S and S != 0:
        add_quque()
        while queue:
            x, y = queue.popleft()
            #print(x,y)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < N and ny >= 0 and ny < N: # 범위 안에 있는 경우 
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y] # 바이러스 전염 
        count += 1
        # print(count)
        # print(graph)
        is_done = True
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 0:
                    is_done = False
        if is_done: # 0이 없으면 종료 
            break
    
    print(graph[X- 1][Y-1])
                         

if __name__ ==  "__main__":
    main()
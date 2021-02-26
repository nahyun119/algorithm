# 계속 테스트 케이스 일부가 오류가 나서 엄청 헤맸다가
# 상어가 이동하면 원래 상어가 있던 자리를 0으로 만들어야하는데
# 이 작업을 하지 않아서 답이 맞지 않았다.. 
# 근데 시간초과가 발생~~~
# 그래서 map을 만들지 않고 bfs를 진행하면서 먹을 수 있는 부분을 다 담고 거리가 짧고 가장 위쪽 ,왼쪽으로 정렬해서 맨 첫번째를 내놓도록
# 먹을 수 있는 부분이 없다면 -1 리턴 

import sys
from collections import deque
from itertools import chain
input = sys.stdin.readline

def move(cx, cy, size, graph): # 지나간다 
    n = len(graph)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((cx, cy, 0))
    visited = [[0] * n for _ in range(n)]
    visited[cx][cy] = 1
    result = []

    while q:
        tx, ty, c = q.popleft()

        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if graph[nx][ny] <= size and visited[nx][ny] == 0:
                    if graph[nx][ny] < size and graph[nx][ny] != 0 : # 먹을 수 있는거 
                        result.append((c + 1, nx, ny))
                    q.append((nx, ny, c + 1))
                    visited[nx][ny] = 1

    result.sort(key = lambda x : (x[0], x[1], x[2]))

    if result:
        return result[0]
    else:
        return (-1, -1, -1)             

def main():
    n = int(input())
    graph = []
    fish_map = {}

    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(n):
            if temp[j] == 9: # 상어 
                start = (i, j)
        graph.append(temp)

    
    size = 2 # 초기 사이즈 2
    cx = start[0]
    cy = start[1]

    time = 0 # 걸린 시간 
    count = 0 # 물고기 먹은 수 

    while True:

        dist, x, y = move(cx, cy, size, graph)
        if x == -1 and y == -1:
            print(time)
            break 

        else:
            graph[cx][cy] = 0
            time += dist 
            count += 1
            if count == size:
                size += 1
                count = 0
            cx = x 
            cy = y
            graph[x][y] = 0
            


        # distance = []
        # min_value = 1e9
        # for value in avail:
        #     d = move(cx, cy, value[0], value[1], size, graph)
        #     if d != -1: # 갈 수 있는 경우 
        #             if d < min_value:
        #                 distance = []
        #                 distance.append((value[0], value[1], d))
        #                 min_value = d 
        #             elif d == min_value:
        #                 distance.append((value[0], value[1], d))
            
        #     distance.sort(key = lambda x : (x[0], x[1])) # 가장 위쪽, 왼쪽을 위해 정렬 

        #     if distance:
        #         x = distance[0][0]
        #         y = distance[0][1]
        #         time += distance[0][2]
        #         graph[cx][cy] = 0 # -> 상어가 이동하므로 원래 있던 자리는 빈칸으로 만들어야한다. 
        #         cx = x 
        #         cy = y 
        #         count += 1
        #         if count == size:
        #             size += 1
        #             count = 0
        #         if graph[x][y] in fish_map:
        #             fish_map[graph[x][y]] = [k for k in fish_map[graph[x][y]] if k != (x, y)] # 업데이트 
        #         graph[x][y] = 0
        #     else:
        #         print(time)
        #         break            

        # for i in range(1, size): # 자신 크기 보다 작은 물고기만 
        #     if i in fish_map:
        #         avail.extend(fish_map[i])

        # if len(avail) == 0: # 먹을 물고기가 없다면 
        #     print(time)
        #     break 

        # else:
            

if __name__ ==  "__main__":
    main()
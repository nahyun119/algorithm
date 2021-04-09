import sys 
from collections import deque
input = sys.stdin.readline 

n, m, t = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]

q = deque()
q.append((0, 0, 0)) # x, y, 시간 
visited[0][0] = 1

min_value = 1e9 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y, count = q.popleft()
    # print(x, y, count)
    if count > t: # 시간 초과면 종료 t시간에 도착해도 구출할 수 있다!!! -> 문제를 꼼꼼히 읽자.ㅣㅣ.
        # min_value = 1e9 # 만약 시간 초과 전에 그람을 만나서 시간을 업데이트 할 수 있으므로
        break 
    
    if x == n - 1 and y == m - 1: # 공주 찾음 
        if min_value > count:
            min_value = count 
        break 
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if visited[nx][ny] == 0 or (nx == n - 1 and ny == m - 1):
                if graph[nx][ny] == 2: # 검 발견! -> 그러면 공주까지 최소 거리 구해서 업데이트하고 그냥 넘어간다. 
                    time = abs(nx - (n - 1)) + abs(ny - (m - 1)) + count + 1 # 공주와의 거리 
                    if time < min_value and time <= t: # 주어진 시간안에 이동할 수 있으면 
                        min_value = time 
                    visited[nx][ny] = 1 # 그래도 방문 표시
                elif graph[nx][ny] == 0: # 검 발견 x! -> 그냥 계속 이동 
                    visited[nx][ny] = 1
                    q.append((nx, ny, count + 1))

if min_value >= 1e9:
    print("Fail")
else:
    print(min_value)

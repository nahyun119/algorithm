import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
remain_cheeze = 0
for i in range(n):
    t = list(map(int, input().split()))
    remain_cheeze += t.count(1) # 남아있는 치즈 수 
    graph.append(t)


def bfs(): # bfs해서 사라지는 치즈들 구하기 
    queue = deque()
    visited = [[0] * m for _ in range(n)]

    for i in [0, n - 1]:
        for j in range(m): # 가장자리 모음
            queue.append((i, j))
            visited[i][j] = 1
    
    for i in range(n):
        for j in [0, m - 1]: # 가장자리 모음
            queue.append((i, j))
            visited[i][j] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    remove_cheeze = []

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0: # 방문하지 않은 경우 
                    if graph[nx][ny] == 1: # 공기에 닿아서 없어지는 치즈 
                        remove_cheeze.append((nx, ny))
                        visited[nx][ny] = 1 # 방문 처리 
                    elif graph[nx][ny] == 0: # 공기인 경우 이동할 수 있도록 
                        visited[nx][ny] = 1 # 방문 처리 
                        queue.append((nx, ny))

    return remove_cheeze

def change(remove_cheeze): # 치즈 업데이트 
    global remain_cheeze
    count = remain_cheeze - len(remove_cheeze) # 남아있는 치즈 업데이트 
    if count <= 0: # 남아있는 치즈가 없는 경우  
        return True
    else: # 남아있는 치즈가 있는 경우 
        remain_cheeze = count # 업데이트
        for x, y in remove_cheeze:
            graph[x][y] = 0 # 공기로 업데이트 
        return False 
    
remove_cheeze = bfs()
if len(remove_cheeze) == 0: # 처음부터 치즈가 없는 경우 
    print(0)
    print(0)
else:
    count = 1
    while True:
        flag = change(remove_cheeze)
        if flag: 
            print(count)
            print(remain_cheeze)
            break
        else:
            count += 1
            remove_cheeze = bfs()
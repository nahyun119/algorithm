from collections import deque
T = int(input())
for t in range(T):
    n, m, r, c, l = map(int, input().split())
    road = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        road.append(temp)
    
    visited = [[0] * m for _ in range(n)]

    q = deque()
    q.append((r, c, 1))
    visited[r][c] = 1
    
    dx = [-1, 1, 0, 0] # 위 아래 왼쪽 오른쪽 
    dy = [0, 0, -1, 1]

    hash_map = {}
    hash_map[1] = [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]] # 위 아래 왼쪽 오른쪽 
    hash_map[2] = [[1, 2, 5, 6], [1, 2, 4, 7], [], []]
    hash_map[3] = [[], [], [1, 3, 4, 5], [1, 3, 6, 7]]
    hash_map[4] = [[1, 2, 5, 6], [], [], [1, 3, 6, 7]]
    hash_map[5] = [[], [1, 2, 4, 7], [], [1, 3, 6, 7]]
    hash_map[6] = [[], [1, 2, 4, 7], [1, 3, 4, 5], []]
    hash_map[7] = [[1, 2, 5, 6], [], [1, 3, 4, 5], []]

    while q:
        x, y, time = q.popleft()
        #print(x, y, time)
        if time == l:
            continue 

        bridge = road[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if visited[nx][ny] == 0 and road[nx][ny] in hash_map[bridge][i]:
                    q.append((nx, ny, time + 1))
                    visited[nx][ny] = 1
    

        
    total = 0

    for i in range(n):
        total += visited[i].count(1)
    #print(total)
    print("#" + str(t + 1), total)
    #print(visited)
from collections import deque
import copy 
T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    
    m = []
    start = []
    max_value = 0
    for j in range(n):
        temp = list(map(int, input().split()))
        v = max(temp)
        if max_value < v:
            start = []
            for i in range(n):
                if temp[i] == v:
                    start.append((j , i))
            max_value = v
        elif max_value == v:
            for i in range(n):
                if temp[i] == v:
                    start.append((j , i))
        m.append(temp)
    
    q = deque()
    for s in start:
        v = [[0] * n for _ in range(n)]
        v[s[0]][s[1]] = 1
        q.append((s[0], s[1], False, m, 0, v))
    # v = [[0] * n for _ in range(n)]
    # v[2][3] = 1
    # q.append((2, 3, False, m, 1, v))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    max_path = 0
    
    while q:
        x, y, flag, graph, count, visited = q.popleft() # flag 0이면 깎지 않음, 1아면 깎음 
        #print(x, y, flag, count, graph, visited)

        max_path = max(max_path, count)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if visited[nx][ny] == 0:
                    if graph[nx][ny] < graph[x][y]:
                        #vi = copy.deepcopy(visited)
                        visited[nx][ny] = 1
                        q.append((nx, ny, flag, graph, count + 1, visited))
                    else:
                        if not flag: # 깎지 않았다면 
                            # if graph[nx][ny] - k < graph[x][y]:
                            #     pre = graph[nx][ny]
                            #     graph[nx][ny] = graph[x][y] - 1
                            #     visited[nx][ny] = 1
                            #     q.append((nx, ny, True, graph, count + 1, visited))
                            #     graph[nx][ny] = pre
                            
                            
                            for j in range(1, k + 1):
                                h = graph[nx][ny] 
                                if h - j < graph[x][y]:
                                    #g = copy.deepcopy(graph)
                                    graph[nx][ny] = h - j
                                    # vi = copy.deepcopy(visited)
                                    visited[nx][ny] = 1
                                    # visited[nx][ny] = 1
                                    q.append((nx, ny, True, graph, count + 1, visited))
                                    graph[nx][ny] = h 
        visited[x][y] = 0
                
    
    print("#" + str(t + 1),  max_path)

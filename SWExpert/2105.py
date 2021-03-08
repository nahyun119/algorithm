# 사각형 모양으로 그려져야한다!!!!!!!1
# 통과는 했는데,,,, 시간 너무 ㅗ오래걸림..,. 에휴 


T = int(input())

def dfs(start, x, y, count, meals, direc):
    global max_value, path
    if direc > 4:
        return 
        
    if start != (x, y): # 처음 시작위치가 아닌경우 
        visited[x][y] = 1
   
    if count != 0 and start[0] == x and start[1] == y and direc <= 4:
        #print(start, x, y, count, meals, direc)
        
        if max_value < count:
            max_value = count
            path = visited
        return 
    
    dx = [1, 1, -1, -1] # 0: 왼쪽 아래 1: 오른쪽 아래, 2: 오른쪽 위, 3: 왼쪽 위 
    dy = [-1, 1, 1, -1]
    

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if visited[nx][ny] == 0 and ((stores[nx][ny] not in meals and start != (nx, ny)) or start == (nx, ny)):
                meals.append(stores[nx][ny])
                if i != direc:
                    dfs(start, nx, ny,  count + 1, meals, direc + 1)
                else:
                    dfs(start, nx, ny, count + 1, meals, direc)
                meals.pop()
    
    visited[x][y] = 0

for t in range(T):
    n = int(input())
    stores = []
    max_value = 0
    for _ in range(n):
        stores.append(list(map(int, input().split())))
    visited = [[0] * n for _ in range(n)]
    path = visited[:]
    for i in range(n):
        for j in range(n):
            if path[i][j] == 0:
                dfs((i, j), i, j, 0, [stores[i][j]], 0)

    if max_value < 4:
        print("#" + str(t + 1), -1)
    else:
        print("#" + str(t + 1), max_value)

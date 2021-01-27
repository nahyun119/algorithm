# 프로그래머스 다이나믹 프로그래밍 3번
# 맨 처음에는 길찾기라서 bfs 이용해서 queue 써서 이동한 곳 담고 그렇게 풀었는데,
# 그렇게 하면 시간초과가 발생한다.
# 다시 dp를 이용해서 했는데, 방문을 안한 경우면 거기서 다음을 갈 수 없으므로 통과 
# 물 웅덩이도 -1로해서 0 이상인 경우만 이동할 수 있도록
# 다음 위치까지 갈 수 있는 경우의 수는 현재 위치에서 갈 수 있는 경우의 수를 더한다. 



def solution(m, n, puddles):
    answer = 0
    
    road = [[0] * m for _ in range(n)]
    
    for puddle in puddles:
        x, y = puddle[0], puddle[1]
        road[y - 1][x - 1] = -1
    
    road[0][0] = 1 # 시작점이니까 1 
    
    for i in range(n):
        for j in range(m):
            #print(road)
            
            if road[i][j] > 0: # 방문 안한 곳이면 
                if i + 1 < n:
                    if road[i + 1][j] != -1: # 물이 아니면
                        road[i + 1][j] += road[i][j]
                if j + 1 < m:
                    if road[i][j + 1] != -1: # 물이 아니면
                        road[i][j + 1] += road[i][j]
    #print(road)
    
#     while queue:
#         x, y = queue.popleft()
        
#         if x + 1 < n and y < m:
#             if road[x + 1][y] != -1:
#                 road[x + 1][y] += 1
#                 queue.append((x + 1, y))
                
#         if y + 1 < m and y < m:
#             if road[x][y + 1] != -1:
#                 road[x][y + 1] += 1
#                 queue.append((x, y + 1))
    
    
    answer = road[n - 1][m -1] % 1000000007
    return answer
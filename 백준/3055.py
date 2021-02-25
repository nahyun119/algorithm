import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check_water(queue, graph, visited, r, c): # 현재 물의 위치를 통해서 다음 시간 물이 차는 위치를 알아낸다. 
    global dx, dy
    q = deque()
    q.extend(queue)
    temp = deque() # 다음에 물이 차는 위치를 담는 배열 
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and nx < r and ny >= 0 and ny < c:
                if visited[nx][ny] == 0 and graph[nx][ny] == '.': # 비어있는 칸만 이동할 수 있다. 
                    temp.append((nx, ny))
                    visited[nx][ny] = 1
                    graph[nx][ny] = '*'
    return temp
    


def main():
    global dx, dy
    r, c = map(int, input().split())
    graph = []
    water = deque()
    for i in range(r):
        temp = list(input().strip())
        for j in range(c):
            if temp[j] == 'D':
                end = (i, j)
            elif temp[j] == 'S':
                start = (i, j)
            elif temp[j] == '*': # 물 
                water.append((i, j))
    
        
        graph.append(temp)
    
    visited = [[0] * c for _ in range(r)]
    water_visited = [[0] * c for _ in range(r)]

    q = deque()
    q.append((start[0], start[1], 0))

    water_map = {}

    water_map[0] = check_water(water, graph, water_visited, r, c)

    while q:
        x, y, dist = q.popleft()
        if (x, y) == end: # 도착한 경우 
            print(dist)
            return 

        if dist not in water_map: # 거리 즉, 시간별로 물이 차는 위치를 구하기 위해서 hash_map 사용 
            w = check_water(water_map[dist - 1], graph, water_visited, r, c)
            water_map[dist] = w

        #print(x, y, dist, water_map[dist])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < r and ny >= 0 and ny < c:
                if visited[nx][ny] == 0 and (nx, ny) not in water_map[dist] and (graph[nx][ny] == '.' or graph[nx][ny] == 'D'):
                    q.append((nx, ny, dist + 1))
                    visited[nx][ny] = 1
            
    
    print("KAKTUS")

if __name__ ==  "__main__":
    main()
# 나는 이차원 리스트를 각각 그래프로 바꿔서 진행했는데,
# 그냥 distacne 를 2차원 리스트로해서 보다 간단하게 구현할 수 있었다.


import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline # n이 125까지인데 그러면 노드 수는 125 * 125 니까 
                           # O(N^3)인 플로이드를 쓰면 매우 느리다 적합하지 않다. 

result = [] # 나중에 결과를 담을 배열 

def dijkstra():
    global result 
    n = int(input())

    dx = [-1, 1, 0, 0] # 상하좌우 이동을 위해 
    dy = [0, 0, -1, 1]

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    

    distance = [[INF] * n for _ in range(n)] # 최단 거리 테이블을 2차원 리스트로 

    x, y = 0, 0
    q = [(graph[x][y], x, y)] # 거리랑 좌표를 추가 
    distance[x][y] = graph[x][y] # 시작점에서의 에너지 소모량 

    while q:
        dis, x, y = heapq.heappop(q)
        if distance[x][y] < dis: # 이미 탐색했음
            continue
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx >= 0 and nx < n and ny >= 0 and ny < n: # 범위 안에 있는경우 
                cost = dis + graph[nx][ny] # (x, y)까지 거리 + (x,y)에서 (nx, ny)로 가는 거리
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
            else:
                continue
    
    result.append(distance[n - 1][n - 1]) # 0에서 맨 마지막 노드까지 가는 비용 + [0][0] 에너지 소모량 



def main():
    T = int(input()) # 테스트 케이스 수 
    for _ in range(T):
        dijkstra()
    
    for i in range(T):
        print(result[i])

if __name__ ==  "__main__":
    main()
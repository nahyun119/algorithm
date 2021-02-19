import sys
import heapq
input = sys.stdin.readline
INF = 1e9
def main():
    m, n = map(int, input().split())

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    graph = []
    for _ in range(n):
        l = input().strip()
        graph.append(list(map(int, l)))
    
    q = []
    distance = [[INF] * m for _ in range(n)]
    distance[0][0] = 0 # 시작점 
    heapq.heappush(q, (0, (0, 0)))
    
    while q:
        dis, x = heapq.heappop(q)
        if distance[x[0]][x[1]] < dis:
            continue
        
        for i in range(4):
            nx = x[0] + dx[i]
            ny = x[1] + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                cost = distance[x[0]][x[1]] + graph[nx][ny]
                if distance[nx][ny] > cost:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, (nx, ny)))
                    
    print(distance[n - 1][m - 1])              
                

if __name__ ==  "__main__":
    main()
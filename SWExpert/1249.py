INF = 1e9
import heapq
def solve():
    n = int(input())

    graph = []
    for _ in range(n):
        graph.append(list(input().strip()))
    
    distance = [[INF] * n for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    distance[0][0] = 0

    x = 0
    y = 0

    q = []
    heapq.heappush(q, (0, x, y))
    while q:
        dis, x, y = heapq.heappop(q)
        if distance[x][y] < dis:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                cost = dis + int(graph[nx][ny])
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost 
                    heapq.heappush(q, (cost, nx, ny))
    
    return distance[n - 1][n - 1]


        

def main():
    T = int(input())
    for i in range(T):
        result = solve()
        print("#" + str(i + 1), result)


if __name__ ==  "__main__":
    main()
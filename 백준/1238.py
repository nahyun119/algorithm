import sys
import heapq

input = sys.stdin.readline
INF = 1e9


def main():
    n, m, x = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    

    def solve(start):
        q = []
        distance = [INF] * (n + 1)
        distance[start] = 0

        heapq.heappush(q, (0, start))

        while q:
            dis, node = heapq.heappop(q)
            if distance[node] < dis:
                continue

            for b, c in graph[node]:
                cost = distance[node] + c 
                if distance[b] > cost:
                    distance[b] = cost
                    heapq.heappush(q, (cost, b))
        
        return distance

    result = solve(x) # x에서 각자 집가는 경로 
    for i in range(1, n + 1):
        if i == x:
            continue
        distance= solve(i) # 각자 집에서 x 가는 경로 
        result[i] += distance[x]

    print(max(result[1:]))
        

if __name__ ==  "__main__":
    main()
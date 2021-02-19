# 1238번이 통과를 했지만,, 뭔가 다익스트라를 모든 도시에 대해서 하는게 걸려서,,
# 한번 줄여보자
# 그래서 나온 결과는 
# 방향을 반대로 한 후 x에서 시작하는 다익스트라 결과를 이용하면 된다. 방향을 반대로하면 x에서 다른 집으로 가는 경우가 원래 방향일 때 다른 집에서 x로 가는 최단 경로이므로! 
# 두번의 다익스트라로 통과할 수 있다. 
# 이렇게 했더니 1332ms -> 84ms 로 확연한 차이를 보였다..

import sys
import heapq

input = sys.stdin.readline
INF = 1e9


def main():
    n, m, x = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    reverse_graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        reverse_graph[b].append((a, c))
    
    def re_solve():
        q = []
        distance = [INF] * (n + 1)
        distance[x] = 0

        heapq.heappush(q, (0, x))

        while q:
            dis, node = heapq.heappop(q)
            if distance[node] < dis:
                continue

            for b, c in reverse_graph[node]:
                cost = distance[node] + c 
                if distance[b] > cost:
                    distance[b] = cost
                    heapq.heappush(q, (cost, b))
        
        return distance

    def solve():
        q = []
        distance = [INF] * (n + 1)
        distance[x] = 0

        heapq.heappush(q, (0, x))

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

    re_result = re_solve() # x에서 각자 집가는 경로 
    result = solve()
    answer = []
    for i in range(1, n + 1):
        answer.append(re_result[i] + result[i])
    
    print(max(answer))
    #print(max(result[1:]))
        

if __name__ ==  "__main__":
    main()
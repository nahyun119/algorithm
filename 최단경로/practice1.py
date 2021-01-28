# 모든 도시 (A, B) 쌍으로 최단 비용을 도출하므로 플로이드 워셜 알고리즘 이용

import sys

INF = int(1e9)
input = sys.stdin.readline # m이 10만개이므로 

def main():
    n = int(input()) # 도시 수
    m = int(input()) # 연결된 노선 수
    
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split()) # a에서 b로 가는데 비용 c
        if graph[a][b] > c: #원래 비용보다 더 작다면
            graph[a][b] = c # 업데이트 
    
    for i in range(1, n + 1):
        graph[i][i] = 0 # 자기 자신은 비용 0으로 
    
    for i in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b]) # 한번에 가는 비용이랑 거쳐서 가는 비용 중 최소로 
    
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] >= INF:
                print(0, end = " ") # 갈 수 없는 곳은 0으로
            else:
                print(graph[a][b], end = " ")
        print()

if __name__ ==  "__main__":
    main()
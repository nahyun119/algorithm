# 모든 정점에 대해서 경로가 있는지 여부를 구하는 문제
# 플로이드 워셜을 사용한다. 100^3 

import sys 
input = sys.stdin.readline 
INF = 1e9

n = int(input())
graph = [[1] * n for _ in range(n)]
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(n):
        if l[j] == 0:
            graph[i][j] = INF


for k in range(n): # 사이로 두는 인덱스를 제일 바깥으로 설정해야 
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


result = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] < INF:
            result[i][j] = 1 
    print(*result[i])
# 모든 노드들에 대해서 다른 모든 노드들까지의 최단 경로를 구하려면 플로이드 워샬 알고리즘을 사용

import sys
input = sys.stdin.readline 
INF = int(1e9)

def main():
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
        for j in range(n):
            if graph[i][j] == 0:
                graph[i][j] = INF
       #print(graph[i])

    # for i in range(n):
    #     graph[i][i] = 0 # 자기 자신은 거리 0으로 초기화인데 지문에서 자기자신은 항상 0이라고 했으므로 
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(n):
        for j in range(n):
            if graph[i][j] == INF:   
                print(0, end = " ")
            else:
                print(1, end = " ")
        print()

if __name__ ==  "__main__":
    main()
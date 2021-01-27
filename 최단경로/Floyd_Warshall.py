# 모든 노드에서부터 다른 모든 노드까지의 최단 경로를 구하는 플로이드 워셜 알고리즘

INF = int(1e9)

def main():
    n = int(input()) # 노드 개수
    m = int(input()) # 간선 개수

    graph = [[INF] * (n + 1) for _ in range(n + 1)] # 그래프 

    for i in range(1, n + 1):
        graph[i][i] = 0 # 자기 자신 거리 0으로 초기화

    for _ in range(m):
        a, b, c = map(int, input().split()) # 간선 정보를 입력 받는다.
        graph[a][b] = c 
    
    for i in range(1, n + 1): # n개의 모든 노드 탐색 
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b]) # a -> b 바로 이동하는 거리, i를 지나쳐서 가는 거리 비교 
    
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] == INF:
                print("갈 수 없음", end = " ")
            else:
                print(graph[a][b], end = " ")
        print()



if __name__ ==  "__main__":
    main()
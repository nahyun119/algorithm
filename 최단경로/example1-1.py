# 예제 1번 플로이드 워셜 알고리즘으로 푼 경우 

INF = int(1e9)

def main():
    N, M = map(int, input().split())

    graph = [[INF] * (N + 1) for _ in range(N + 1)]

    for _ in range(M): # 그래프 입력 받기 
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1
    
    X, K = map(int, input().split())
    
    for i in range(1, N + 1):
        graph[i][i] = 0 # 자기 자신은 0으로 초기화 
    
    for i in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])
    
    distance = graph[1][K] + graph[K][X]

    if distance >= INF:
        print(-1)
    else:
        print(distance)



if __name__ ==  "__main__":
    main()
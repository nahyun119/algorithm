# 모든 학생에 대해서 성적 비교 정보를 이용해 모든 다른 학생한테 갈 수 있는지 없는지
# 확인하는 것이기 때문에 플로이드 이용(모든 학생 고려)

import sys

INF = int(1e9)
input = sys.stdin.readline # 정보가 최대 10000개

def main():
    n, m = map(int, input().split())

    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split()) # a 성적 < b 성적 
        graph[a][b] = -1 # a < b이므로 -1 
        graph[b][a] = 1 # 반대로 b입장에서는 a보다 크기때문에 
    
    for i in range(1, n + 1):
        graph[i][i] = 0 # 자기 자신은 0으로 
    
    for i in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if graph[a][i] >= INF: # a와 i 사이 순위를 모르면 
                    if graph[a][b] == 1: # a > b인 경우 
                        if graph[b][i] == 1: # i < b 라면 i < b < a 이므로 순위를 알 수 있다. 
                            graph[a][i] = 1 # a > i이므로 
                            graph[i][a] = -1 # i < a이므로 
                    if graph[a][b] == -1 : # a < b인 경우 
                        if graph[b][i] == -1: # b < i 라면 a < b < i 이므로 순위를 알 수 있다. 
                            graph[a][i] = -1 # a < i이므로 
                            graph[i][a] = 1 # i > a이므로 

               
    count = 0 # 정확한 순위를 알 수 있는 애들 
    for i in range(1, n + 1):
        #print(graph[i])
        if INF not in graph[i][1: ]:  # 0번을 제외 1번부터 다른 학생들로 모두 갈 수 있다면 순위를 알 수 있다.
            count += 1
    
    print(count)

        


if __name__ ==  "__main__":
    main()

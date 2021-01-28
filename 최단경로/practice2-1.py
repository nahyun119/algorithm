# practice2.py에서 원래 플로이드 워셜 알고리즘 점화식 써서 
# 거리가 있다면 갈 수 있도로 했는데, 뭔가 답이 제대로 안나와서
# 응용문제라고 생각해서 경우의 수 확인하고 업데이트 하도록 했다.
# 근데 플로이드 점화식을 써서 진행할 수 있다. 

import sys

INF = int(1e9)
input = sys.stdin.readline # 정보가 최대 10000개

def main():
    n, m = map(int, input().split())

    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split()) # a 성적 < b 성적 
        graph[a][b] = 1 # a < b이므로 -1 
        #graph[b][a] = 1 # 반대로 b입장에서는 a보다 크기때문에 
    
    for i in range(1, n + 1):
        graph[i][i] = 0 # 자기 자신은 0으로 
    
    for i in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

    #print(graph)
    result = 0 # 정확한 순위를 알 수 있는 애들 
    for a in range(1, n + 1):
        count = 0 # 한 학생에 대해서 다른 모든 학생으로 이동할 수 있는지 
        for b in range(1, n + 1):
            if graph[a][b] != INF or graph[b][a] != INF: # 둘 중 한 명이라도 순위를 알 수 있으면 
                count += 1 
            if count == n: # 모든 학생으로 갈 수 있으면 순위를 정확히 알 수 있다. 
                result += 1

    
    print(result)

        


if __name__ ==  "__main__":
    main()

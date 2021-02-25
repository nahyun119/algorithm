# 모든 도시에 대해서 갈 수 있는지 구하기 위해 플로이드 워셜 알고리즘을 사용함
# 그래서 둘중 하나라도 거리가 무한이라면 못가는 것이기 때문에 NO를 출력하고 종료
# 그렇지 않은 경우 YES 

# 근데 유니온 파인드로 풀 수 있다고 해서 이렇게 풀어보자 -> 1976-1.py

import sys

input = sys.stdin.readline
INF = 1e9
def main():
    n = int(input())
    m = int(input())

    graph = []
    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(n):
            if temp[j] == 1:
                graph.append((i, j))
        graph.append((i, i))
    
    distance = [[INF] * n for _ in range(n)]
    citys = list(map(int, input().split()))
    
    for g in graph:
        distance[g[0]][g[1]] = 1
        distance[g[1]][g[0]] = 1


    for k in range(n):
        for a in range(n):
            for b in range(n):
                distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])
    

    for i in range(m - 1):
        if distance[citys[i] - 1][citys[i + 1] - 1] == INF or distance[citys[i] - 1][citys[i + 1] - 1] == INF:
            print("NO")
            return 
    print("YES")
    #print(distance)
    


if __name__ ==  "__main__":
    main()
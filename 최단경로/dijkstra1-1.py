import sys
import heapq # 최단 거리 노드를 찾기 위한 우선순위 큐 라이브러리 

input = sys.stdin.readline # 입력 속도를 빠르게 하기위해 대치 
INF = int(1e9) # 무한을 의미하는 값으로 약 10억을 선언 

def main():
    n, m  = map(int, input().split()) # 노드 갯수, 간선 갯수 

    start = int(input())
    graph = [[] for i in range(n + 1)] # 간선 정보를 저장하기 위해 선언

    distance = [INF] * (n + 1) # 최단 거리 테이블 선언, 무한으로 초기화

    for _ in range(m):
        a, b, c = map(int, input().split()) # a에서 b로 가는 거리 비용이 c 
        graph[a].append((b, c))

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dis, node = heapq.heappop(q) # 제일 최단 거리인 노드 
        if distance[node] < dis: # 이미 처리된 경우 
            continue # 다음 최단 거리 노드로 이동 
        for i in graph[node]:
            cost = dis + i[1] # 비용 구하기
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # 갱신하면 갱신한 노드와 거리를 queue에 저장
                
    for i in range(1, n + 1): # start 에서 시작하는 최단 경로 출력
        if distance[i] == INF:
            print("갈 수 없음")
        else:
            print(distance[i])


            





if __name__ ==  "__main__":
    main()
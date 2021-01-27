# 특정 노드에서부터 다른 모든 노드까지의 최단 경로르 구하는 다익스트라 알고리즘 
# 탐색을 위해 이동해야하는 다음 노드를 찾기 위해서
# distance 리스트를 순차적으로 탐색해서 가장 최단 거리인 노드를 찾는 과정이 필요 
# 단순히 리스트를 이용해서 최단 경로를 찾으려면 순차 탐색을 진행하므로 O(노드 개수)만큼 걸린다.
# 이 과정을 빠르게 하기 위해 우선순위 큐를 사용한다. -> 우선 순위 큐를 이용하면 O(log노드 개수) 만큼 걸리므로
# 훨씬 더 빨라진다 --> dijkstra1-1.py 


import sys

input = sys.stdin.readline # 입력 속도를 빠르게 하기위해 대치 
INF = int(1e9) # 무한을 의미하는 값으로 약 10억을 선언 


def get_small_node(visited, distance):
    n = len(distance)
    min_value = INF
    index = 0
    for i in range(1, n):
        if distance[i] < min_value and not visited[i]: # 거리가 최소이면서 방문하지 않은 경우
            min_value = distance[i]
            index = i

    return index




def main():
    n, m  = map(int, input().split()) # 노드 갯수, 간선 갯수 

    start = int(input())
    graph = [[] for i in range(n + 1)] # 간선 정보를 저장하기 위해 선언

    visited = [False] * (n + 1) # 방문 여부 저장 
    distance = [INF] * (n + 1) # 최단 거리 테이블 선언, 무한으로 초기화

    for _ in range(m):
        a, b, c = map(int, input().split()) # a에서 b로 가는 거리 비용이 c 
        graph[a].append((b, c))

    distance[start] = 0
    visited[start] = True
    #print(graph[start])
    for i in graph[start]: # 시작 노드와 연결된 노드 거리 비용 업데이트
        distance[i[0]] = i[1]
    
    for i in range(n - 1): # 시작 노드를 제외한 n - 1개 노드에 대해서 시작 # 다익스트라 함수 
        node = get_small_node(visited, distance)
        visited[node] = True
        for j in graph[node]: # 최단 거리인 노드로 이동 
            cost = distance[node] + j[1]   # 원래 있던 값이랑 새로 구한 거리 중 최솟값으로 업데아트
            if cost < distance[j[0]]:
                distance[j[0]] = cost

    for i in range(1, n + 1): # start 에서 시작하는 최단 경로 출력
        if distance[i] == INF:
            print("갈 수 없음")
        else:
            print(distance[i])


            





if __name__ ==  "__main__":
    main()
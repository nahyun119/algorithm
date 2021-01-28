# 2차원 리스트에서 최소 비용 거리를 구하라해서 bfs, dfs같은데
# 가는데 비용이 각각 달라서 최단 경로 이용하는 것이라 생각
# n * n개 각 칸을 노드라 생각하고 상하좌우로 이동할 수 있기 때문에
# 상히좌우로 연결된 칸들과 간선이 있다고 생각하고 연결된 칸 값을 비용이라 생각 

import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline # n이 125까지인데 그러면 노드 수는 125 * 125 니까 
                           # O(N^3)인 플로이드를 쓰면 매우 느리다 적합하지 않다. 

result = [] # 나중에 결과를 담을 배열 

def dijkstra():
    global result 
    n = int(input())
    
    v = n * n # 노드 수 
    
    dx = [-1, 1, 0, 0] # 상하좌우 이동을 위해 
    dy = [0, 0, -1, 1]

    energy = []
    for _ in range(n):
        energy.append(list(map(int, input().split())))
    
    graph = [[] for i in range(v)] # 0부터 시작하므로 
    distance = [INF] * v

    node = 0
    for i in range(n): # 간선 정보 입력 
        for j in range(n):
            #print(node)
            for k in range(4):
                nx = i + dx[k] 
                ny = j + dy[k]
                if nx >= 0 and nx < n and ny >= 0 and ny < n: # 범위 안에 있는 경우 
                    if k == 0: # 상이면 노드번호 - n
                        graph[node].append((node - n, energy[nx][ny])) # 노드번호랑 비용 추가 
                    elif k == 1: # 하면 노드번호 + n
                        graph[node].append((node + n, energy[nx][ny])) # 노드번호랑 비용 추가 
                    elif k == 2: # 좌면 노드번호 - 1
                        graph[node].append((node - 1, energy[nx][ny])) # 노드번호랑 비용 추가 
                    else: # 우면 노드번호 + 1
                        graph[node].append((node + 1, energy[nx][ny])) # 노드번호랑 비용 추가 
            node += 1

    q = []
    distance[0] = 0 # 0부터 시작이므로 
    heapq.heappush(q, (0, 0))

    while q:
        dis, node = heapq.heappop(q)
        if distance[node] < dis: # 이미 탐색했음
            continue
        
        for i in graph[node]:
            cost = dis + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    result.append(distance[-1] + energy[0][0]) # 0에서 맨 마지막 노드까지 가는 비용 + [0][0] 에너지 소모량 



def main():
    T = int(input()) # 테스트 케이스 수 
    for _ in range(T):
        dijkstra()
    
    for i in range(T):
        print(result[i])

if __name__ ==  "__main__":
    main()
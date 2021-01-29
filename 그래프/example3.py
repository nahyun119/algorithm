# 커리큘럼을 이수하기 위한 강의마다 최소 시간을 구한다.
# 방향이 있는 애들을 순서대로 정렬하므로 위상정렬을 이용

from collections import deque

def main():
    n = int(input()) # 강의 수 

    indegree = [0] * (n + 1) # 진입 차수 초기화 

    graph = [[] for _ in range(n + 1)]
    time = [0] * (n + 1) # 시간 정보를 담는 테이블 


    for i in range(1, n + 1):
        data = list(map(int, input().split()))
        time[i] = data[0]

        #print(data[1: ])
        for d in data[1: -1]: # 1번째부터 마지막 전까지 
            indegree[i] += 1
            graph[d].append(i) # 선수과목이 해당 과목을 가리키도록 그래프에 추가 

    total_time = [0] * (n + 1)
    q = deque()
    
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i) # 0인 노드 큐에 추가 
    
    while q:
        node = q.popleft()
        total_time[node] += time[node] # 자기 자신 시간 추가 
        #print(total_time[1: ], node, total_time[node])
        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
            if total_time[i] == 0: # 아무도 거치지 않은 경우 
                total_time[i] += total_time[node]
            else: # 원래 있는 값이랑 새로 들어온 값 중 최솟값으로 원래 값이 있다면 해당 노드로 이미 비용이 결정된 것 
                #print(total_time[i], total_time[node])
                total_time[i] = min(total_time[i], total_time[node])


    #print(indegree)
    #print(graph)

    for i in range(1, n + 1):
        print(total_time[i])
                



if __name__ ==  "__main__":
    main()
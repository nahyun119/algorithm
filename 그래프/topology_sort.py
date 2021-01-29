# 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 위상 정렬 알고리즘
from collections import deque



def main():
    v, e = map(int, input().split())

    indegree = [0] * (v + 1) # 노드 수만큼 진입 차수 테이블

    graph = [[] for _ in range(v + 1)] # 그래프

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b) # a -> b
        indegree[b] += 1 # a에서 b로 들어오므로 b의 진입차수 증가 

    def topology_sort():
        result = [] # 결과 저장하는 배열 
        q = deque() # 진입차수가 0인 노드들을 담는 queue

        for i in range(1, v + 1):
            if indegree[i] == 0:
                q.append(i) # queue에 진입차수가 0인 노드를 넣는다. 

        while q: # q가 빌 때까지
            node = q.popleft()
            result.append(node) # 결과에 추가 
            for i in graph[node]: # node에서 연결된 간선을 제거 
                indegree[i] -= 1 # node와 연결된 진입차수를 뺀다
                if indegree[i] == 0: # 진입차수가 0이라면 q에 넣는다.
                    q.append(i)
        
        for re in result:
            print(re, end = ' ')

            
    topology_sort()


if __name__ ==  "__main__":
    main()
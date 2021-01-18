# 시간 초과가 발생한다
# 그래서 input.split() 대신 import sys를 해서 입력을 받았다. 
# 입력이 100만줄이 입력될 수 있기 때문에
# input().split() 대신 sys.stdin.readline().rstrip().split() 을 이용 
import sys 
from collections import deque
def main():
    #N, M, K, X = map(int, input().split())
    N, M, K, X = map(int, sys.stdin.readline().rstrip().split())

    graph = [[] for _ in range(N)] # 도시 수만큼 배열 초기화 
    for value in range(M):
        #x, y = map(int, input().split())
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[x - 1].append(y - 1) 
    
    queue = deque()
    cost = [-1] * N 

    queue.append(X - 1)
    cost[X - 1] = 0

    while queue:
        node = queue.popleft()
        
        for value in graph[node]:
            if cost[value] < 0: # 연결된 해당 노드에 방문하지 않은 경우
                cost[value] = cost[node] + 1
                queue.append(value)
        
    #print(cost)
    is_in = False 
    #result = []
    for index in range(N):
        if cost[index] == K:
            #result.append(index + 1)
            print(index + 1)
            is_in = True
    if not is_in:
        print(-1)
        return
        
            

    

if __name__ ==  "__main__":
    main()
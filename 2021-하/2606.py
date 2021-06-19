import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
v = int(input()) # 컴퓨터 쌍의 수 

graph = [[] for _ in range(n + 1)]

for i in range(v):
    a, b = map(int, input().split())
    graph[a].append(b) # 연결 표시
    graph[b].append(a)

queue = deque()
visited = [0 for i in range(n + 1)]
queue.append(1) # 1번부터 시작이므로 
visited[1] = 1

while queue:
    node = queue.popleft()

    for k in graph[node]:
        if visited[k] == 0: # 방문하지 않은 경우
            visited[k] = 1
            queue.append(k)


print(len([x for x in visited if visited[x] == 1]) - 1) # 1번 컴퓨터를 제외해야하므로 -1 한다. 





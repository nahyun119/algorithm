import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
min_value = 1e9

queue = deque()
queue.append((n, 0))

visited = [False] * 100001
visited[n] = True 

while queue:
    number, count = queue.popleft()
    #print(number)

    if number == k:
        if min_value > count:
            min_value = count 
        break

    if number - 1 >= 0 and not visited[number - 1]:
        queue.append((number - 1, count + 1))
        visited[number - 1] = True 
    if number + 1 <= 100000 and not visited[number + 1]:
        queue.append((number + 1, count + 1))
        visited[number + 1] = True
    if number * 2 <= 100000 and not visited[number * 2]:
        queue.append((number * 2, count + 1))
        visited[number * 2] = True 

print(min_value)
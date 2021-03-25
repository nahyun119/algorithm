import sys
from collections import deque
input = sys.stdin.readline 
n = int(input())
queue = deque()
for i in range(n):
    order = input().strip()
    order = order.split()

    if order[0] == "push":
        queue.append(order[1])
    elif order[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif order[0] == "size":
        print(len(queue))
    elif order[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif order[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])

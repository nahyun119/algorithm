import sys
import heapq # -> 기본적으로 min heap이므로 max heap을 구현하려면 우선순위에 -1을 곱한다. 
from collections import deque

input = sys.stdin.readline

result = []
def solve():
    global result 
    n, m = map(int, input().split())
    documents = list(map(int, input().split()))
    
    q = deque()
    answer = []
    for i in range(n):
        q.append((documents[i], i))

    count = 1
    while True:
        max_value = max(q)
        priority, index = q.popleft()
        #print(max_value, priority, index)
        if priority < max_value[0]:
            q.append((priority, index))
        else:
            if index == m:
                break 
            count += 1 # 프린트한 경우만 카운트 
    
    result.append(count)
    #print(count)



def main():
    global result 
    T = int(input())
    for _ in range(T):
        solve()
    
    for r in result:
        print(r)

if __name__ ==  "__main__":
    main()
import sys
input = sys.stdin.readline 

n = int(input())

for i in range(n + 1):
    result = i + sum(list(map(int, str(i))))
    # print(result)
    if result == n:
        print(i)
        break 

    if i == n: # 마지막까지 온 경우 
        print(0)

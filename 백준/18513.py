# bfs이용해서 푸는거 같은데,,, 시간초과가 엄청난다,, 어떻게 해야할까,,ㅠㅠ 

import sys 
input = sys.stdin.readline 
MAX_VALUE = 100000000

n, k = map(int, input().split())
water = list(map(int, input().split()))

water.sort()
visited = []
visited.extend(water)


dis = 1
result = 0
while k > 0:
    for i in range(n):
        if water[i] - dis >= -MAX_VALUE and water[i] - dis not in visited:
            k -= 1
            result += dis 
            visited.append(water[i] - dis)
            if k == 0:
                break 
        if water[i] + dis <= MAX_VALUE and water[i] + dis not in visited:
            k -= 1
            result += dis 
            visited.append(water[i] + dis)
            if k == 0:
                break
    dis += 1

        
print(result)
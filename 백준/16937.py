import sys
input = sys.stdin.readline

h, w = map(int, input().split())
n = int(input())
stickers = []
for i in range(n):
    x, y = map(int, input().split())
    stickers.append((x, y))

result = -1
for i in range(n - 1):
    for j in range(i + 1, n):
        # i, j를 그냥 넣는 경우 
        size = stickers[i][0] * stickers[i][1] + stickers[j][0] * stickers[j][1]
        if stickers[i][0] + stickers[j][0] <= h and max(stickers[i][1], stickers[j][1]) <= w: # 가로로 
            if result < size:
                result = size 
        if stickers[i][0] + stickers[j][0] <= w and max(stickers[i][1], stickers[j][1]) <= h: # 세로로 
            if result < size:
                result = size 
        # i 그대로, j 돌려서
        if stickers[i][0] + stickers[j][1] <= h and max(stickers[i][1], stickers[j][0]) <= w: # 가로로 
            if result < size:
                result = size 
        if stickers[i][0] + stickers[j][1] <= w and max(stickers[i][1], stickers[j][0]) <= h: # 세로로 
            if result < size:
                result = size 
        # i 돌려서 j 그대로 
        if stickers[i][1] + stickers[j][0] <= h and max(stickers[i][0], stickers[j][1]) <= w: # 가로로 
            if result < size:
                result = size 
        if stickers[i][1] + stickers[j][0] <= w and max(stickers[i][0], stickers[j][1]) <= h: # 세로로 
            if result < size:
                result = size 
        
        # i 돌려서, j 돌려서
        if stickers[i][1] + stickers[j][1] <= h and max(stickers[i][0], stickers[j][0]) <= w: # 가로로 
            if result < size:
                result = size 
        if stickers[i][1] + stickers[j][1] <= w and max(stickers[i][0], stickers[j][0]) <= h: # 세로로 
            if result < size:
                result = size 

if result == -1:
    print(0)
else:
    print(result)

        

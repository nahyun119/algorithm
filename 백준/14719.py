import sys
input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))

water = 0

for i in range(1, w - 1):
    # 왼쪽에서 제일 큰 높이
    left = blocks[i]
    for j in range(i - 1, -1, -1):
        if blocks[j] > left:
            left = blocks[j]
    # 오른쪽에서 제일 큰 높이
    right = blocks[i]
    for j in range(i + 1, w):
        if blocks[j] > right:
            right = blocks[j]
    
    height = min(right, left)
    # print(height)
    water += height - blocks[i]

print(water)

                
            


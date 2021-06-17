import sys
input = sys.stdin.readline

k, n = map(int, input().split()) # 입력 

line_list = []
max_line = -1
for i in range(k):
    l = int(input())
    if max_line < l:
        max_line = l
    line_list.append(l)
    
ans = -1

def binary_search(start, end):
    global ans
    if start > end:
        return 
    # print(start, end)

    m = (start + end) // 2
    
    total = 0
    for i in range(k):
        total += line_list[i] // m 
    # print(total, n, m, ans)
    if total >= n: # n개 이상을 만들 수 있는 경우 길이를 늘린다. 범위를 오른쪽으로 이동 
        if ans < m: # 길이가 더 큰 경우 
            ans = m 
            binary_search(m + 1, end)
    else: # n개를 만들 수 없는 경우, 길이를 줄인다. 범위를 왼쪽으로 이동 
        binary_search(start, m - 1)


binary_search(1, max_line)

print(ans)

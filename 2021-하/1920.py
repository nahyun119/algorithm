import sys
input = sys.stdin.readline 

n = int(input())
a = list(map(int, input().split()))
m = int(input())

b = list(map(int, input().split()))

a.sort()


def binary_search(start, end, value):
    global a, b
    
    while start <= end:
        mid = (start + end) // 2
        if mid >= n: # 범위 벗어나는 경우 종료 
            break
        # print(start, end, mid, n, a[mid])
        if a[mid] == value: # 값을 찾았다면 
            print(1)
            return 
        
        if a[mid] > value: # 값이 작다면 왼쪽으로 이동
            end = mid - 1
        elif a[mid] < value: # 값이 크다면 오른쪽으로 이동 
            start = mid + 1
        
    
    print(0)


for i in b:
    binary_search(0, n, i)

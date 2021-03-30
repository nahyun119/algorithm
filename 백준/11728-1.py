# 인덱스 이용해서 풀었는데 
# 그냥 합치고 정렬하는게 더 빠른거 같다...
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = a + b
a.sort()
print(*a)
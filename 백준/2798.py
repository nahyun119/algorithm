import sys
input = sys.stdin.readline 
n, m = map(int, input().split())
cards = list(map(int, input().split()))


result = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            value = cards[i] + cards[j] + cards[k]
            if abs(m - result) > abs(m - value) and value <= m: # m을 넘지않으면서 m이랑 가까운 수 
                result = value 


print(result)

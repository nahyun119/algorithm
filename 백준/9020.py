# 소수를 찾으므로 n은 10000까지 이므로 에레토스테네스의 체를 다시 이용해보자 
import sys
input = sys.stdin.readline
T = int(input())
numbers = []
for t in range(T):
    numbers.append(int(input()))

max_value = max(numbers) + 1
sieve = [True] * max_value

m = int(max_value ** 0.5)

for i in range(2, m + 1): # 약수 갯수만큼 진행
    if sieve[i] == True:
        for j in range(i + i, max_value, i):
            sieve[j] = False 

for i in numbers:
    for j in range(i // 2, 1, -1): # 소수는 2까지이므로 
        if sieve[j] == True and sieve[i - j] == True:
            print(j, i - j)
            break
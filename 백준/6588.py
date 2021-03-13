import sys
input = sys.stdin.readline
numbers = []
while True:
    n = int(input())
    if n == 0:
        break 
    numbers.append(n)

max_value = max(numbers)
sieve = [True] * max_value

m = int(max_value ** 0.5)
for i in range(2, m + 1): # 홀수에 대해서만
    if sieve[i] == True:
        for j in range(i + i, max_value, i):
            sieve[j] = False 

for i in numbers:
    flag = False 
    for j in range(3, max_value, 2): # 홀수만 
        if sieve[j] == True and sieve[i - j] == True and (i - j) % 2 != 0:
            print(str(i) + " = " + str(j) + " + " + str(i - j))
            flag = True 
            break 
    if not flag:
        print("Goldbach's conjecture is wrong.") # 나타내지 못하는 경우 
        

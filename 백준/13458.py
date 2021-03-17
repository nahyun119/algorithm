import sys
import math
input = sys.stdin.readline 
n = int(input())

people = list(map(int, input().split()))

a, b = map(int, input().split()) # 총감독관, 부감독관 

vice_total = 0

for i in range(n):
    if people[i] > a:
        value = math.ceil((people[i] - a) / b)
        vice_total += value

print(vice_total + n)
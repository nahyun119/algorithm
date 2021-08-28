import sys
import math
input = sys.stdin.readline

n = int(input()) # 시험장 수 
people = list(map(int, input().split())) # 시험장 응시자 수 

direc, p_direc = map(int, input().split()) # 총 감독관 응시생 수, 부감독관 응시생 수

count = n # 총 몇 명이 필요한지
for i in range(n):
    if people[i] > direc:
        count += math.ceil((people[i] - direc) / p_direc)

print(count)
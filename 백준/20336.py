import sys
import itertools 
input = sys.stdin.readline 
n = int(input())
snow = list(map(int, input().split()))
snow.sort()

# 이중 반복문으로 먼저 첫번째 눈사람 만들고 
# 그리고 투 포인터를 이용해서 두번째 눈사람 파악 

result = 1e9

for i in range(n):
    for j in range(i + 3, n):
        start = i + 1
        end = j - 1
        while start < end:
            temp = (snow[i] + snow[j]) - (snow[start] + snow[end])
            if abs(temp) < result:
                result = abs(temp) 
            
            if temp < 0: # 첫번째 눈사람보다 두번째 눈사람이 더 큰 경우 두번째 눈사람을 줄인다. 
                end -= 1
            else: # 첫번째 눈사람이 두번째 눈사람보다 더 큰 경우 두번째 눈사람을 늘린다. 
                start += 1

print(result)
                
            



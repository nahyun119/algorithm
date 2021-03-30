# 한 명을 반복문 돌리고 
# 나머지 두 명을 투 포인터 알고리즘 써서 진행하면 될 것 같다.
import sys
input = sys.stdin.readline 

n = int(input())
ability = list(map(int, input().split()))
ability.sort()

count = 0
for i in range(n - 2):
    start = i + 1
    end = n - 1

    index = n 

    while start < end:
        temp = ability[i] + ability[start] + ability[end]   
        if temp == 0:
            if ability[start] == ability[end]: # 두 개가 같은 경우 
                count += end - start 
            else: # 다른 경우 오른쪽이랑 같은 값 찾기
                if index > end:
                    index = end 
                    while index >= 0 and ability[index - 1] == ability[end]:
                        index -= 1
                count += end - index + 1
            start += 1
        elif temp < 0: # 0보다 작으면 ability[i] < ability[start] + ability[end]를 더 크게 
            start += 1
        else: # 0보다 크면 ability[i] > ability[start] + ability[end], ability[start] + ability[end]를 더 작게 
            end -= 1

print(count)
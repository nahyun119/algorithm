# 쉬익쉬익 시간초과!@~@~@~@
import sys
input = sys.stdin.readline 

n, d, k, c = map(int, input().split()) # 접시의 수, 초밥 수, 연속해서 먹는 수, 쿠폰 번호 
# 쿠폰 번호 포함안하고 최대 k를 먹을 수 있도록 

foods = []
result = -1
start = 0
end = -1
check = False 

for i in range(n):
    food = int(input())
    if food == c:
        check = True 
    foods.append(food)
    end += 1
    if end >= k - 1:
        temp = set(foods)
        length = len(temp)
        if check: # 쿠폰에 해당하는 값이 포함된 경우 
            if result < length:
                result = length
        else: # 쿠폰이 없는 경우
            if result < length + 1:
                result = length + 1
        if foods[start] == c:
            check = False 
        foods.pop(0) # 맨 처음 원소 제거 


print(result)
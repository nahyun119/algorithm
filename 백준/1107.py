from collections import deque
n = int(input())
m = int(input())
not_avail = []
if m != 0: # 고장난 버튼이 없을수도 있다. 
    not_avail = list(map(int, input().split()))

check = [1] * 10
for i in range(m):
    check[not_avail[i]] = 0

#print(check)
answer = abs(n - 100) # 채널이동으로만 가는 경우 

# 브루트포스문제 
# 채널의 최대는 500,000이고 0 ~ 9999999까지 모든 숫자의 경우의수를 확인하기 위해 
for number in range(1000001):
    s_number = str(number)
    for i in range(len(s_number)):
        if check[int(s_number[i])] == 0: # 사용못하는 숫자 발견하면 반복문 종료 
            break 
        elif i == len(s_number) - 1: # 마지막까지 온 경우 
            answer = min(abs(number - n) + len(s_number), answer)

print(answer)

    




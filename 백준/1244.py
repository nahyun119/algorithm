import sys
import math
input = sys.stdin.readline 
n = int(input())
status = list(map(int, input().split()))
m = int(input())
student = []
for i in range(m):
    sex, number = map(int, input().split())
    if sex == 1: # 남자라면 스위치 번호 배수를 모두 상태 변경 
        for j in range(number, n + 1, number):
            if status[j - 1] == 0:
                status[j - 1] = 1
            else:
                status[j - 1] = 0
    elif sex == 2: # 여자라면 자기 자신을 중심으로 대칭이루는 구간 
        r = min(number, n - number + 1) 
        number -= 1 
        # print(r)
        for j in range(r):
            if status[number - j] == status[-n + number + j]:
                # print(number - j, -n + number + j)
                if j == 0: # 원래 그 번호라면 
                    if status[number] == 0:
                        status[number] = 1
                    else:
                        status[number] = 0
                else:
                    if status[number - j] == 0:
                        status[number - j] = 1
                        status[-n + number + j] = 1
                    else:
                        status[number - j] = 0
                        status[-n + number + j] = 0
                # print(*status)
            else:
                break 
# 한 줄에 20개씩 출력
r = math.ceil(n / 20)
for i in range(r):
    if i == r - 1:
        print(*status[20 * i: ])
    else:
        print(*status[i * 20: (i + 1) * 20])



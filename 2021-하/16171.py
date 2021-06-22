import sys
input = sys.stdin.readline

question = input().strip()
answer = input().strip()

real = ''
flag = False 
for s in question:
    if 48 <= ord(s) <= 57: # 숫자인 경우 
        continue 
    else: # 문자인 경우 
        real += s
        # print(real, answer, real.find(answer)) 
        if real.find(answer) != -1: #순서대로 진행한 경우 동일하다면 
            flag = True 
            break 
if flag:
    print(1) 
else:
    print(0)

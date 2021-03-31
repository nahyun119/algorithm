import sys
input = sys.stdin.readline 

n = int(input())

todo = []
max_day = -1
for i in range(n):
    s, e = map(int, input().split())
    if e > max_day:
        max_day = e 
    todo.append((s, e, e - s + 1))
calendar = [[0] * 365 for _ in range(1001)] # 명령어 최대 갯수 1000개 

todo.sort(key = lambda x : (x[0], -x[2]))

max_index = -1 # 최대 명령어가 ~~ 
for i in range(n):
    s, e, duration = todo[i]
    index = 0
    while True: # 일정을 넣을 수 있는 공간 찾기 
        flag = True
        for j in range(s - 1, e, 1):
            if calendar[index][j] != 0:
                flag = False 
                break 
        if not flag:
            index += 1
        else:
            break 
    if index > max_index:
        max_index = index 
    for j in range(s - 1, e, 1):
        calendar[index][j] = 1 
x = 0
y = 0
result = 0 

for i in range(max_day):
    col = [calendar[k][i] for k in range(max_index + 1)]
    if 1 not in col:
        # print(x,y)
        result += x * y 
        x = 0 
        y = 0
    else:
        index = 0
        while calendar[index][i] != 0:
            index += 1
        if y < index:
            y = index 
        x += 1

result += x * y
print(result)

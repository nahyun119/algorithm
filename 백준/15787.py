import sys
input = sys.stdin.readline 
n, m = map(int, input().split())
train = [[0] * 20 for _ in range(n)]

for t in range(m):
    temp = list(map(int, input().split()))
    order, arg = temp[0], temp[1:]
    # print(order, arg)
    if order == 1:
        i, x = arg[0] - 1, arg[1]
        if train[i][x - 1] == 0: # i번째 기차에 x번째 사람이 없다면 사람을 태운다. 
            train[i][x - 1] = 1
    elif order == 2:
        i, x = arg[0] - 1, arg[1]
        if train[i][x - 1] == 1: # i번째 기차에 x번째 사람이 있다면 하차시킨다.
            train[i][x - 1] = 0
    elif order == 3:
        i = arg[0] - 1
        train[i] = [0] + train[i][:19] # 뒤로 한 칸씩 이동 대신 맨 마지막 사람은 하차 
    elif order == 4:
        i = arg[0] - 1
        train[i] = train[i][1:] + [0]

temp = []
count = 0
for i in range(n):  
    if train[i] not in temp:
        temp.append(train[i])
        count += 1
# print(temp)
print(count)

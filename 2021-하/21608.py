import sys 
input = sys.stdin.readline
n = int(input())

students = [[] for _ in range(n ** 2 + 1)]
order = []
for i in range(n ** 2): # 학생 수 n^2
    t = list(map(int, input().split()))
    order.append(t[0])
    students[t[0]] = t[1:]


seat = [[-1] * n for _ in range(n)] # 실제 자리 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 인접한 칸 중 좋아하는 학생이 많은 순서대로, 빈 칸 한번에 계산 
def first(number):
    like = 0
    like_list = []
    for x in range(n):
        for y in range(n):
            count = 0
            empty = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < n and 0 <= ny < n:
                    if seat[nx][ny] in students[number]:
                        count += 1
                    if seat[nx][ny] == -1: # 주위가 빈 칸인 경우    
                        empty += 1

            if seat[x][y] == -1: # 빈 자리인 경우에만  
                if count > like:
                    like = count 
                    like_list = [(x, y, empty)]
                elif count == like:
                    like_list.append((x, y, empty))

    return like_list

# 여러 개라면 빈 칸이 여러 개인 칸 
for i in order:
    s_list = first(i)
    s_list.sort(key = lambda x : (-x[2], x[0], x[1])) # 빈 칸 수, 행, 열 번호로 정렬 
    nx = s_list[0][0]
    ny = s_list[0][1]

    seat[nx][ny] = i 

# 만족도 계산 
total = 0
for i in range(n):
    for j in range(n):
        count = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if seat[nx][ny] in students[seat[i][j]]: # 좋아하는 학생이라면 
                     count += 1
        if count > 0:
            total += 10 ** (count - 1)

# print(seat)
print(total)
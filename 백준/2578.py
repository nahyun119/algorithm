import sys
input = sys.stdin.readline 

bingo_map = {}
for i in range(5):
    temp = list(map(int, input().split()))
    for j in range(5):
        bingo_map[temp[j]] = (i, j)

numbers = [] # 한 줄로 받도록 
for i in range(5):
    numbers.extend(list(map(int, input().split())))

visited = [[0] * 5 for _ in range(5)]

def check():
    count = 0
     
    for i in range(5): # row 검사 
        flag = True
        if 0 in visited[i]:
            flag = False 
        if flag:
            count += 1

    for i in range(5): # col 검사 
        flag = True 
        for j in range(5):
            if visited[j][i] == 0:
                flag = False 
        if flag:
            count += 1
    
    flag1 = True
    flag2 = True 
    for i in range(5):
        if visited[i][i] == 0:
            flag1 = False 
        if visited[i][4 - i] == 0:
            flag2 = False 

    if flag1:
        count += 1
    if flag2:
        count += 1
    
    if count >= 3:
        return True 
    return False 

    



for i in range(25):
    x, y = bingo_map[numbers[i]]
    visited[x][y] = 1 
    if i >= 4: # 5개 이하인 경우는 확인할 필요가 없으므로 
        if check():
            print(i + 1)
            break    
    
    

            
                

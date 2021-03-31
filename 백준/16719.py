# 뭔가 dfs를 사용해서 진행하면 될 것 같다.
# 어렵다 어려워ㅠㅠㅠㅠ

import sys
input = sys.stdin.readline

string = list(input().strip())
temp = string[:]
length = len(string)

visited = [0 for _ in range(length)]

def dfs(pre_index, index, value):
    if index < 0 and index > length:
        return value
    visited[index] = 1
    print(value)

    # 오른쪽 부분 
    min_right = 'z' * 100
    min_index = -1
    for i in range(index, length):
        if visited[i] == 0 and min_right > string[i]:
            min_right = string[i]
            min_index = i 
    
    if min_index != -1:
       dfs(index, min_index, value + min_right)
    

    # 왼쪽 부분 
    min_left = 'z' * 100
    min_index = -1 

    for i in range(pre_index + 1, index):
        if visited[i] == 0 and min_left > string[i]:
            min_left = string[i]
            min_index = i 

    if min_index != -1:
        temp = -1
        for k in range(len(value)):
            if value[k] == string[index]:
                temp = k
                break 
        dfs(index, min_index, value[:temp] + min_left + value[temp:])
        print(value[temp], value)
min_value = min(string)
min_index = string.index(min_value)

dfs(0, min_index, min_value)
    
    




    

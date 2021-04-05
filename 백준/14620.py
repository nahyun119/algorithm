import sys 
import copy 
import itertools
input = sys.stdin.readline 
n = int(input())

garden = []
for i in range(n):
    garden.append(list(map(int, input().split())))

min_value = 1e9

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_location(number):
    q, r = divmod(number, n) # 행 열 
    location = set([(q, r)])
    flag = True 
    for i in range(4):
        nx = q + dx[i]
        ny = r + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            location.add((nx, ny))
        else:
            flag = False
            break  
    
    if flag:
        return location 
    else:
        return set([]) 

def get_price(locations):
    total = 0
    l_locations = list(locations)
    for i in range(15):
        cx, cy = l_locations[i]
        total += garden[cx][cy]
    
    return total 

for i in range(n*n - 2):
    first_location = get_location(i)
    len1 = len(first_location)
    if len1 == 0:
        continue 
    for j in range(i + 1, n * n - 1):
        second_location = get_location(j)
        len2 = len(second_location)
        if len2 == 0:
            continue 
        for k in range(j + 1, n * n):
            third_location = get_location(k)
            len3 = len(third_location)
            # print(first_location, second_location, third_location)
            if len3 == 0:
                continue 
            else:
                total_location = first_location | second_location | third_location
                if len(total_location) == 15: # 15개 자리를 차지 정상적인 경우   
                    total = get_price(total_location)
                    # print(total)
                    if total < min_value:
                        min_value = total 

print(min_value)
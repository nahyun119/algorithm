# 비트 연산을 이용해서 풀어보자 
# 주의할 점! 책이름에 알파벳 숫자 갯수도 알아야한다!!!! 만약 NNETWORK가 입력인데 전공책 이름이 NETWORK인 경우 -1이어야
# in으로만 처리하면 안된다.
import sys
import copy
input = sys.stdin.readline

W = input().strip()
n = int(input())

q = []
names = []
for i in range(n):
    price, name = map(str, input().split())
    q.append((int(price), name))
    name_map = {}
    for na in name:
        if na in name_map:
            name_map[na] += 1
        else:
            name_map[na] = 1 
    names.append(name_map)
 

min_value = 1e9
for i in range(1, (1 << n)): # 3이라면 001 010 011 100 101 110 111 이렇게 7개가 존재 1~ 2^3 - 1까지 
    temp = W 
    total = 0
    for j in range(0, n):
        w = ''
        if i & (1 << j) != 0:
            # print(j)
            price, name = q[j]
            temp_map = copy.deepcopy(names[j])
            for t in temp: # 단어가 여러개 일 수 있다.
                if t not in temp_map:
                    w += t 
                else:
                    if temp_map[t] <= 0:
                        w += t 
                    else:
                        temp_map[t] -= 1
            temp = w  
            total += price   
        else:
            continue 
    if len(temp) == 0:
        if min_value > total:
            min_value = total 

if min_value >= 1e9:
    print(-1)
else:
    print(min_value)

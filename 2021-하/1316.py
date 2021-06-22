import sys 
input = sys.stdin.readline 

n = int(input())

count = 0

for i in range(n):
    s = input().strip()
    pre = s[0] # 바로 이전 문자 
    pre_list = set([s[0]])
    length = len(s)
    flag = True
    for j in s[1:]:
        if j in pre_list and pre == j: # 이미 이전 문자열에 있지만 이전 문자랑 동일한 경우 연속인 경우  
            pre_list.add(j)
        elif j not in pre_list and pre != j: # 처음 등장하는 문자인 경우    
            pre_list.add(j)
            pre = j 
        else: # 위의 경우의 수에 모두 해당하지 않는 경우  
            flag = False 
            break 
        
    if flag:
        # print(s)
        count += 1

print(count)
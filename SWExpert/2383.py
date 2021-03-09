# 너무 어렵다ㅠㅠㅠ다시 해보자 

T = int(input())
for t in range(T):
    n = int(input())
    board = []

    p = [] #사람위치 
    s = [] #계단위치 

    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(n):
            if temp[j] == 1: # 사람이라면 
                p.append((i, j))
            elif temp[j] > 1: # 계단이라면 
                s.append((i, j, temp[j]))

    wait = []

    for i in range(len(p)):
        x, y = p[i][0], p[i][1]
        dis = 1e9
        s_index = -1
        for j in range(len(s)):
            sx, sy = s[j][0], s[j][1]
            distance = abs(x - sx) + abs(y - sy)
            if distance + s[j][2] < dis + s[s_index][2]:
                dis = distance
                s_index = j
        #heapq.heappush(wait, (dis, i, s_index, 0, 0))
        wait.append((dis, i, s_index, 0, 0))
    
    stairs = [[] for _ in range(len(s))]

    visited = [0] * len(p)
    max_value = 0
    count = 0
    
    while True:
        if 0 not in visited:
            break 

        for i in range(len(p)):
            dis, p_index, s_index, time, s_time = wait[i]
            if visited[p_index] == 0:
                if s_time == s[s_index][2]: # 시간이 다 된 경우 
                    #print(count, wait[i])
                    visited[p_index] = 1 
                    stairs[s_index].remove(p_index)
                    if max_value < count - 1:
                        max_value = count - 1
                        continue

                if count == dis: # 거리가 지난 경우, 계단에 들어갈 수 있다.    
                    if s_time == 0: # 계단에 들어가지 않은 경우 
                        if len(stairs[s_index]) >= 3: # 대기해야
                            wait[i] = (dis, p_index, s_index, time + 1, s_time)
                        else: # 바로들어갈 수 있다. 
                            stairs[s_index].append(p_index)
                            wait[i] = (dis, p_index, s_index, time + 1, s_time + 1)
                    else: # 계단에 들어간 경우  
                        wait[i] = (dis, p_index, s_index, time + 1, s_time + 1)
                elif count > dis:
                    if s_time == 0 : # 들어갈 시간 지났는데 아직 계단 안들어간 경우 
                        if len(stairs[s_index]) >= 3: # 대기해야
                            wait[i] = (dis, p_index, s_index, time + 1, s_time)
                        else: # 바로들어갈 수 있다. 
                            stairs[s_index].append(p_index)
                            wait[i] = (dis, p_index, s_index, time + 1, s_time + 1)
                    else:
                        wait[i] = (dis, p_index, s_index, time + 1, s_time + 1)
                print(count, wait[i])  
        count += 1

    print(max_value ) 


        
    
        
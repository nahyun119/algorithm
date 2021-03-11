from collections import deque
## 풀긴 했는데, 시간 초과ㅠㅠㅠㅠㅠㅠ -> 더 해보자
T = int(input())
for t in range(T):
    n, m, limit = map(int, input().split())

    dead = deque() # 죽은 상태 
    active = deque() # 활성 상태 
    non_active = deque() # 비활성 상태 
    visited = [] # 어떤 상태이든 있는 경우 
    for i in range(n): # 비활성 상태 담기 
        temp = list(map(int, input().split()))
        for j in range(m):
            if temp[j] != 0:
                non_active.append((i, j, temp[j], temp[j]))
                visited.append((i, j))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    time = 0
    while time <= limit:

        # 비활성화 -> 활성 처리 
        new_non_active = []
        for i in range(len(non_active)):
            x, y, start, cost = non_active[i] # 위치, 시작 시간, 비용 
            if time >= start:
                active.append((x, y, start + cost, time)) # 위치, 활성화 끝 시간, 활성화 시작 시간 
            else:
                new_non_active.append((x, y, start, cost))

        non_active = new_non_active

        # 활성화 -> 번식, 죽음 
        new_active = []

        for j in range(len(active)):
            x, y, end, start = active[j]

            if time == start + 1: # 번식을 첫 1시간 동안 진행 
                for k in range(4): # 번식 
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if (nx, ny) not in visited:
                        # if (nx, ny) in hash_map:
                        #     h_start, h_end = hash_map[(nx, ny)]
                        #     if end == h_end and h_end - h_start < end - start:
                        #         hash_map[(nx, ny)] = [end, start]
                        # else:
                        #     hash_map[(nx, ny)] = [start, end]
                        non_active.append((nx, ny, time + (end - start), end - start))
                        visited.append((nx, ny))

                    # if (nx, ny) not in visited: # 어떤 상태도 아니어야한다.  
                    #     non_active.append((nx, ny, time + (end - start), end - start)) # end + cost -> end - start == cost 시작 시간 , cost 
                    #     visited.append((nx, ny))
                    #     pre_end = end
                    #     pre_start = start
                    # else: 
                    #     if (nx, ny, pre_start + 1 + (pre_end - pre_start), pre_end - pre_start) in non_active: # non_active에 있는 경우   
                    #         if pre_end == end and pre_end - pre_start < end - start: # cost 비용이 더 큰 경우   
                    #             non_active.remove((nx, ny, pre_start + 1 + (pre_end - pre_start), pre_end - pre_start))
                    #             non_active.append((nx, ny, time + (end - start), end - start))
                    #             pre_end = end
                    #             pre_start = start

            if time >= end: # 끝난 경우 
                dead.append((x, y))
            else:
                new_active.append((x, y, end, start))

        # for nx, ny in hash_map:
        #     h_start, h_end = hash_map[(nx, ny)]
        #     visited.append((nx, ny))
        #     non_active.append((nx, ny, time + h_end - h_start, h_end - h_start))

        active = new_active
        time += 1
        
    result = len(non_active) + len(active)
    print(result)
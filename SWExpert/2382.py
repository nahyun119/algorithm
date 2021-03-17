from collections import deque
T = int(input())
for t in range(T):
    n, m, k = map(int, input().split()) # 셀의 수, 격리 시간, 군집 수 
    queue = deque()
    
    for i in range(k):
        x, y, size, direc = map(int, input().split())
        queue.append((x, y, size, direc, 0))
    # 1: 상, 2: 하, 3: 좌, 4: 우 


    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # print("===========================")
    for i in range(m):
        hash_map = {}

        for j in range(len(queue)):
            x, y, size, direc, time = queue[j]

            nx = x + dx[direc - 1]
            ny = y + dy[direc - 1]

            if nx == 0 or nx == n - 1 or ny == 0 or ny == n - 1: # 가장 자리
                size = size // 2
                
                if direc == 1:
                    direc = 2
                elif direc == 2:
                    direc = 1
                elif direc == 3:
                    direc = 4
                elif direc == 4:
                    direc = 3
                
                if size > 0:
                    hash_map[(nx, ny)] = [(nx, ny, size, direc, time + 1)]
            else:
                if (nx, ny) in hash_map:
                    hash_map[(nx, ny)].append((nx, ny, size, direc, time + 1))
                else:
                    hash_map[(nx, ny)] = [(nx, ny, size, direc, time + 1)]

        #print(hash_map)
        queue = []
        for nx, ny in hash_map:
            if len(hash_map[(nx, ny)]) > 1:
                max_value = 0
                value = 0
                max_direc = -1

                for v in hash_map[(nx, ny)]:
                    value += v[2]
                    if max_value < v[2]:
                        max_value = v[2]
                        max_direc = v[3]
                queue.append((nx, ny, value, max_direc, i + 1))
            else:
                queue.append((nx, ny, hash_map[(nx, ny)][0][2], hash_map[(nx, ny)][0][3], hash_map[(nx, ny)][0][4]))
        
                    
    
    result = 0
    #print(queue)
    for i in range(len(queue)):
        result += queue[i][2]
    print("#" + str(t + 1), result)                         


                

        
        
        
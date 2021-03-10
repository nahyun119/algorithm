T = int(input())
for t in range(T):
    m, a = map(int, input().split())
    move_a = [0]
    move_b = [0]
    move_a += list(map(int, input().split()))
    move_b += list(map(int, input().split()))
     
    wifi = []
    for _ in range(a):
        x, y, c, p = map(int, input().split())
        wifi.append((x, y, c, p))
    
    dx = [0, 0, 1, 0, -1] # 이동 x, 상 우 하 좌 
    dy = [0, -1, 0, 1, 0]

    d_x = [0, 0]
    d_y = [-1, 1]

    road = [[0] * 10 for _ in range(10)]

    wifi_position = []

    for i in range(a): # 무선랜 영향 미치는 곳 체크 
        x, y, c, p = wifi[i]
        w = set()
        start = [(x - 1, y - 1)]
        for j in range(c, -1, -1):
            new = []
            for sx, sy in start:
                w.add((sx, sy))
                for u in range(1, j + 1):
                    for k in range(2):
                        nx = sx + d_x[k] * u
                        ny = sy + d_y[k] * u
                        if nx >= 0 and nx < 10 and ny >= 0 and ny < 10:
                            #print(nx, ny)
                            w.add((nx, ny))

                if sx == x - 1:
                    if sx - 1 >= 0 and sx - 1 < 10:
                        new.append((sx - 1, sy))
                    if sx + 1 >= 0 and sx + 1 < 10:
                        new.append((sx + 1, sy))
                else:
                    if sx > x - 1 :
                        if sx + 1 >= 0 and sx + 1 < 10:
                            new.append((sx + 1, sy))
                    else:
                        if sx - 1 >= 0 and sx + 1 < 10:
                            new.append((sx - 1, sy))
            start = new
            
        wifi_position.append(w)
    #print(wifi_position)

    
    ax = 0
    ay = 0
    bx = 9
    by = 9

    # 시작 위치에서도 체크 
    

    total = 0
    for i in range(m + 1):
        ax = ax + dx[move_a[i]]
        ay = ay + dy[move_a[i]]

        bx = bx + dx[move_b[i]]
        by = by + dy[move_b[i]]

        avail_a = []
        avail_b = []
        for j in range(a):
            if (ax, ay) in wifi_position[j]:
                avail_a.append((wifi[j][3], j))
            if (bx, by) in wifi_position[j]:
                avail_b.append((wifi[j][3], j))

        avail_a.sort(key = lambda x : -x[0])
        avail_b.sort(key = lambda x : -x[0])
        
        max_value = 0

        if avail_a and avail_b:
            for av, ai in avail_a:
                for bv, bi in avail_b:
                    if ai == bi:
                        value = av 
                        if value > max_value:
                            max_value = value
                    else:
                        value = av + bv 
                        if value > max_value:
                            max_value = value 

        elif not avail_a and avail_b:
            max_value = avail_b[0][0]
        elif avail_a and not avail_b:
            max_value = avail_a[0][0]

        #print(ax, ay, bx, by, max_value)
        total += max_value
        
    print("#" + str(t + 1), total)


T = int(input())
for t in range(T):
    p, g = map(int, input().split())
    
    value = max(p, g)

    positions = []
    n = 1
    x, y = 1, 1
    while True:
        #print(positions)
        if len(positions) >= value:
            break 
        for i in range(n):
            positions.append((x, y))
            x += 1
            y -= 1

        n += 1
        x = 1
        y = n
    
    sx = positions[p - 1][0] + positions[g - 1][0]
    sy = positions[p - 1][1] + positions[g - 1][1]
    #print(positions[p - 1], positions[g - 1])
    if (sx, sy) not in positions:
        while True :
            if (sx, sy) in positions:
                break
            
            for i in range(n):
                positions.append((x, y))
                x += 1
                y -= 1
            n += 1
            x = 1
            y = n
        print("#" + str(t + 1), positions.index((sx, sy)) + 1)
    else:
        print("#" + str(t + 1), positions.index((sx, sy)) + 1)
        
    


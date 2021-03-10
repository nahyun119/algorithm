T = int(input())
# p, g의 최댓값이 10000이므로 10000까지 담기 위해서는 가로,세로 400
positions = [0] * 400
for i in range(1, 400 - 1):
    positions[i] = positions[i - 1] + i

for t in range(T):
    p, g = map(int, input().split())
    
    value = max(p, g)
    x = -1
    y = -1
    for i in range(1, 400 - 1):
        if value > positions[i] and value <= positions[i + 1]:
            x = i 
            break 
    
    p_p = []
    g_p = []
    for i in range(1, len(positions)):
        if p_p and g_p:
            break
        if not p_p and p <= positions[i]:
            gab_p = positions[i] - p 
            p_p = [1 + gab_p, i - gab_p]
        if not g_p and g <= positions[i]:
            gab_g = positions[i] - g
            g_p = [1 + gab_g, i - gab_g]
    
    #print(p_p, g_p)

    y = p_p[0] + g_p[0]
    x = p_p[1] + g_p[1]

    result = 0
    # 갭차이 계산 
    for i in range(y - 1):
        result += x + i 

    print("#" + str(t +1), result + positions[x])

    

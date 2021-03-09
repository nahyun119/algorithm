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
    
    

    for i in range(positions[x + 1] - positions[x]):
        if value == temp:
            y = i 
            break 
        


    

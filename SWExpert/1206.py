for t in range(1):
    n = int(input())
    buildings = list(map(int, input().split()))

    result = 0

    for i in range(2, n - 2): # 왼쪽 2개 오른쪽 2개는 건물이 지어지지 않는다.
        height = buildings[i]
        left1 = buildings[i - 2]
        left2 = buildings[i - 1]
        right1 = buildings[i + 1]
        right2 = buildings[i + 2]
        value = max(left1, left2, right1, right2)
        if height - value > 0:
            result += height - value 
    
    print("#" + str(t + 1), result)

            

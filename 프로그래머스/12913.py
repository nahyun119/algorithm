def solution(land):
    answer = 0

    # 항상 최고점을 선택하도록
    
    for i in range(1, len(land)):
        for j in range(4):
            if j == 0:
                land[i][j] += max(land[i - 1][1], land[i - 1][2], land[i - 1][3])
            elif j == 1:
                land[i][j] += max(land[i - 1][0], land[i - 1][2], land[i - 1][3])
            elif j == 2:
                land[i][j] += max(land[i - 1][0], land[i - 1][1], land[i - 1][3])
            else:
                land[i][j] += max(land[i - 1][0], land[i - 1][1], land[i - 1][2])
                
    #print(land)
            
        
    answer = max(land[-1])
    return answer
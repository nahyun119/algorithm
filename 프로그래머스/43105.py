def solution(triangle):
    answer = 0
    
    length = len(triangle)
    
    for i in range(length - 2, -1, -1):
        for j in range(i + 1):
            #print(i, j)
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    
    #print(triangle)
    answer = triangle[0][0]
    return answer
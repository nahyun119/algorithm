def rotate(key):
    N = len(key[0])
    
    rot = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rot[j][N-1-i] = key[i][j]
    return rot

def solution(key, lock):
    answer = True
    
    N = len(lock[0])
    M = len(key[0])
    
    row_index = 0
    col_index = 0
    
    
    while col_index < N:
        row_index = 0
        while row_index < N:
            for value in range(4):
                rot = rotate(key)
                sum = 0
                #print(rot)
                r = min(N - row_index, M)
                c = min(N - col_index, M)
                for i in range(r):
                    for j in range(c):
                        sum += rot[i][j] + lock[i + row_index][j + col_index]
                if sum == r * c:
                    return True
                #print(sum)
                key = rot
            row_index += 1
        col_index += 1
        
    return False
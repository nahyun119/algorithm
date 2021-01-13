def rotate(key):
    N = len(key[0])
    
    rot = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rot[j][N-1-i] = key[i][j]
    return rot

def check(new_lock):
    l = len(new_lock) // 3
    for i in range(l, l * 2):
        for j in range(l, l*2):
            if(new_lock[i][j] != 1):
                return False
    return True
    
def solution(key, lock):
    answer = True
    
    N = len(lock[0])
    M = len(key[0])
    
    row_index = 0
    col_index = 0
    
    # 원래 자물쇠 크기에 3배 크기로 새로운 자물쇠 생성 
    new_lock = [[0] * (N * 3) for _ in range( N *3)]
    
    for i in range(N):
        for j in range(N):
            new_lock[i + N][j + N] = lock[i][j]
    
    while col_index + M <= (N * 3):
        row_index = 0
        while row_index + M <= (N * 3):
            for value in range(4):
                rot = rotate(key)
                sum = 0
                for i in range(M):
                    for j in range(M): # 원래는 sum해서 합으로 하려고 했는데
                        new_lock[i + row_index][j + col_index] += rot[i][j]
                if check(new_lock) == True:
                        return True
                for i in range(M):
                    for j in range(M): # 원래는 sum해서 합으로 하려고 했는데
                        new_lock[i + row_index][j + col_index] -= rot[i][j]      
                key = rot
            row_index += 1
        col_index += 1
        
    return False
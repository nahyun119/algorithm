# lock 에 있는 홈 부분 패턴을 이용해서 같은 패턴이 있는지 확인하도록 짰는데,
# 이 문제는 완전 탐색 문제로 그냥 key 배열을 lock 배열 위에 옮겨가면서 비교한 후에 합이 모두 1인지 아닌지를 확인하면 된다.
# -> 다음에 다시 풀어보기 

def pattern(lock):
    
    is_first = True
    
    lock_pattern = []
    # lock에 있는 key pattern 
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0 and is_first:
                lock_pattern.append((i, j))
                is_first = False
            elif lock[i][j] == 0 and not is_first:
                lock_pattern.append((i - lock_pattern[0][0], j - lock_pattern[0][1])) # 현재 0인 위치랑 맨 처음에 발견한 0의 위치랑 거리 차이를 리스트에 추가 
            else: 
                continue
    # 기준인 원소 위치 0으로 초기화     
    lock_pattern[0] = (0,0)

    return lock_pattern
    
    

def solution(key, lock):
    answer = True
    
    
    N = len(lock[0])
    rot_right = [[0] * N for _ in range(N)]
    rot_left = [[0] * N for _ in range(N)]
    
    
    for i in range(N):
        for j in range(N):
            rot_right[j][N-1-i] = lock[i][j]
            rot_left[N-1-j][i] = lock[i][j]
    
    # lock에서 제일 처음으로 0인 원소의 위치를 기준으로 다른 0인 애들이랑 
    # 행, 열이 얼마나 차이나는지 저장하는 배열 -> lock에서의 key 패턴 구하기 
    lock_pattern = pattern(lock) # lock에서 기준이 되는 홈 패턴
    left_pattern = pattern(rot_left) # lock 왼쪽으로 회전
    right_pattern = pattern(rot_right) # lock 오른쪽으로 회전 

    
    # key에 돌기가 없는 경우, lock에 홈이 없는 경우, key의 돌기가 lock의 홈 보다 작은 경우 
    # 풀 수 없다. 
    
#     for 
#     if key.count(1) == 0 or lock.count(0) == 0 or key.count(1) < lock.count(0):
    
#         return False
    
    

    
    # key에 있는 1인 원소를 기준으로 각각 패턴 구하기 
    # 패턴 구하면서 key pattern에 lock pattern이 있는 경우 종료 
    
    
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == 1:
                key_pattern = []
                key_pattern.append((i, j))
                for k in range(len(key)): # 기준 원소를 기준으로 패턴 구하기 
                    for l in range(len(key)):
                        if key[k][l] == 1: # 기준인 원소 위치 제외 
                            print(i, j, k, l)
                            key_pattern.append((k - key_pattern[0][0], l - key_pattern[0][1]))
                # 기준 원소 0으로 초기화 
                key_pattern[0] = (0,0)
                temp = {}
                temp = set(key_pattern)
                key_pattern = list(temp)
                
                #print(lock_pattern, left_pattern, right_pattern, key_pattern)
                left_count = 0
                right_count = 0
                lock_count = 0
                for i in range(len(lock_pattern)):
                    if lock_pattern[i] in key_pattern:
                        lock_count += 1
                    if left_pattern[i] in key_pattern:
                        left_count += 1
                    if right_pattern[i] in key_pattern:
                        right_count += 1
                if lock_count == len(lock_pattern) or left_count == len(left_pattern) or right_count == len(right_pattern):
                    return True
                        
    
    return False
        
    
    
    #return answer
def solution(N, stages):
    fail = [(0, 0)] * (N + 1) # 0은 냅두고 1부터 N + 1까지 

    stages.sort()

    length = len(stages) # 총 도전한 사용자 수 
    pre_count = stages.count(1) # 이전 스테이지 도전중인 사람 수 
        
    fail[1] = (1, pre_count / length) # 1번 스테이지 먼저 저장 

    for value in range(2, N + 1):
        cu_count = stages.count(value) # 현재 스테이지 도전 중인 사람 수 
        length -= pre_count # 이전 스테이지 도전한 사람 수 빼면 현재 스테이지 도전한 사람 수 
        #print(pre_count, cu_count, length)
        if length <= 0: # 혹시나 0보다 작아진 경우 0으로 나누면 런타임 에러 발생하므로 
            length = 1
        fail[value] = (value, cu_count / length)
        pre_count = cu_count # 현재 도전중인 사람 수를 이전 스테이지 도전한 사람 수로 업데이트 
    
    fail = fail[1: N + 1]

    fail.sort(key = lambda x : -x[1])
    
    answer = list(map(lambda x : x[0], fail))
    
    return answer
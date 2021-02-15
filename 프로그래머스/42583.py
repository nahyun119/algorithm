from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    wait = deque(truck_weights) # 대기 큐 
    
    queue = deque()
    
    queue.append((0, wait[0]))
    count = 1
    wait.popleft()
    
    while queue:
        #print(count, queue, wait)
        total_weight = 0
        q = list(queue)
        queue = deque()
        for time, we in q: # 시간 업데이트 
            r_time = time + 1
            total_weight += we # 무게 구하기 
            if r_time < bridge_length: # 길이이상이면 뺀다. 
                queue.append((r_time, we))
            else: # 빠진 트럭 무게 제외
                total_weight -= we 
        if wait:
            w = wait[0]
            if not queue: # 빈 경우
                queue.append((0, w))
                wait.popleft()
            else:
                if total_weight + w <= weight:
                    queue.append((0, w))
                    wait.popleft()
                      
        count += 1
            
    answer = count
    
    return answer
import heapq

def solution(scoville, K):
    answer = 0
    
    q = []
    for s in scoville:
        heapq.heappush(q, s)
    is_done = False    
    while q: 
        s = heapq.heappop(q)
        if not q:
            if s >= K:
                is_done = True
            break
        if s < K: # 맨처음 원소가 작다면 
            s2 = heapq.heappop(q)
            heapq.heappush(q, s + s2 * 2)
            answer += 1
        else:
            is_done = True
            break
            
    if not is_done:
        return -1
    return answer
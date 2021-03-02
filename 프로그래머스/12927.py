# q에서 max 값을 계속 -1 로 해서 최대한 값을 비슷하게 유지 
import heapq
def solution(n, works):
    answer = 0
    
    q = []
    for w in works:
        heapq.heappush(q, -w)
    #print(q)
    
    for i in range(n):
        if q:
            num = heapq.heappop(q)
            num += 1
            if num != 0:
                heapq.heappush(q, num)
    if not q:
        return 0
    else:
        for num in q:
            answer += num**2
    
    return answer
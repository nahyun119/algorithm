import heapq

def get_max(q):
    temp = []
    while q:
        value = heapq.heappop(q)
        if q: # 마지막이 아니라는 의미
            heapq.heappush(temp, value)
    return temp
            

def solution(operations):
    
    q = []

    
    for operation in operations:
        a, b = operation.split(" ")
        
        if a == 'I':
            heapq.heappush(q, int(b))
        elif a == 'D':
            if q:
                if int(b) == -1:
                    heapq.heappop(q)
                elif int(b) == 1: # 최댓값 삭제 
                    q = get_max(q)    
    
    if not q:
        return [0, 0]
    else:
        return [max(q), min(q)]
    #return answer
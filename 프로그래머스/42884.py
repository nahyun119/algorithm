import heapq

def solution(routes):
    answer = 0
    
    q = []
    visited = [0] * len(routes)
    
    for index, route in enumerate(routes):
        heapq.heappush(q, (-1 * route[0], -1 * route[1], index))
    count = 0
    
    while 0 in visited:
        start, end, index = heapq.heappop(q)
        if visited[index] == 1: # 이미 차량이 지나는 곳은 제외 
            continue
        for i in range(len(routes)):
            s = routes[i][0]
            e = routes[i][1]
            if s <= -start and -start <= e: # 사이에 있으면 
                visited[i] = 1
        count += 1
    answer = count
    return answer
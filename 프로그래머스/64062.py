
def get_next(stones, index, k):
    nx = 1
    n = len(stones)
    while stones[index + nx] == 0 and index + nx < n:
        nx += 1
    if n - 1 - index <= k and stones[-1] == 0:
        return index + k
        
    return index + nx 

def solution(stones, k):
    answer = 0
    n = len(stones)
    
    if n == 1:
        return stones[0]
    
    stones = [x - 1 for x in stones]
    count = 1
    current_index = get_next(stones, -1, k)
    
    while True:
        if current_index >= n - 1:
            count += 1
            current_index = get_next(stones, -1, k)
        
        stones[current_index] -= 1
        next_index = get_next(stones, current_index, k)
        
        if next_index - current_index > k:
            break 
        current_index = next_index 
        
    answer = count
    return answer
def solution(n, times):
    answer = 0
    
    max_value = max(times)
    start = 1
    end = max_value * n
    
    result = end 
    
    while start <= end:
        mid = (start + end) // 2
        
        total = 0
        
        for time in times:
            total += mid // time
            if total >= n:
                break 
                
        if total >= n:
            result = mid
            end = mid - 1
        elif total < n:
            start = mid + 1
            
    #print(result)
    answer = result
    return answer
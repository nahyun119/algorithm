# 값이 엄청 크므로 이진탐색 이용!!

def solution(stones, k):
    answer = 0
    
    start = 0
    end = 200000000

    
    result = []
    while start <= end:
        mid = (start + end) // 2
        temp = [x - mid for x in stones]
        
        count = 0
        is_impo = True
        
        for value in temp:
            
            if value <= 0:
                count += 1
                if count >= k:
                    is_impo = False
                    break 
            else:
                count = 0
                
        #print(mid, is_impo, temp)                 
        if not is_impo:
            end = mid - 1
        else:
            result.append(mid + 1)
            start = mid + 1
            
    #print(result)   -> 계속 1씩 덜 들어가서 확인해보니까 mid랑 뭔가 안맞았다. 그래서 mid + 1을 결과에 넣었더니 성공     
    answer = max(result)
    return answer
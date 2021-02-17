# 풀긴했는데, 시간이 조금 걸리는 것 같다!
# 시간을 줄여보자,, 

def solution(citations):
    
    answer = 0
    
    n = len(citations)
    
    h_index = 0
    
    for i in range(max(citations)):
        temp = [x for x in citations if x >= i]
        #print(i, h_index, temp)
        if i <= len(temp):
            h_index = i
            

    answer = h_index            
    
    return answer
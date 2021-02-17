def solution(citations):
    
    answer = 0
    
    n = len(citations)
    
    h_index = 0
    
#     for i in range(max(citations), -1, -1):
#         temp = [x for x in citations if x >= i]
#         #print(i, h_index, temp)
#         if i <= len(temp):
#             if h_index > i:
#                 return h_index
#             h_index = i
        
#     answer = h_index 
    
    # 역순으로 뒤집어서 citations[i]랑 i를 비교해서 작은 값을 선택한다. 
    
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
    
    #return answer
ㅋimport math 
def solution(s):
    answer = 0
    
    unit = 1 # 단위 문자 수 몇 개 단위인지
    
    # 문자열 길이가 1인 경우는 압축할 필요가 없으므로 return 1 
    # 예외 잘 살펴보기 
    if(len(s) == 1):
        return 1
    
    result_list = []
    
    while unit <= len(s) // 2: # 가장 큰 단위는 문자열의 반 그 이후는 원래 문자열과 동일  
        index = 1 # 단위 문자열 인덱스 
        pre_s = "" # 이전 단위 문자열 저장 
    
        count = 0 # 단위 문자열 갯수 
        
        result = "" # 단위마다 결과 
        
        while index <= math.ceil(len(s) / unit) + 1: # +1을 한 이유는 맨 마지막 단위 문자열을 result에 추가하기 위해, 맨 마지막 단위 문자열인 경우 s[(index - 1) * unit : last_index] 이게 ""라 항상 다르므로 count에 맞게 result에 추가될 수 있다. 
            last_index = min(index * unit, len(s))
            # print(index, pre_s, s[(index - 1) * unit : last_index])
            if not pre_s: # 이전 문자열이 없는 경우, 즉 맨 처음인경우 
                pre_s = s[(index - 1) * unit : last_index]
                count = 1
            elif pre_s and pre_s == s[(index - 1) * unit : last_index]: # 다음 문자열 단위랑 같은 경우 
                count += 1
                #print(index, pre_s, count)
                #pre_s = s[(index - 1) * unit : index * unit]
            elif pre_s and pre_s != s[(index - 1) * unit : last_index]: # 다음 문자열과 다른 경우 
                if count == 1:
                    result += pre_s
                else:
                    result += str(count) + pre_s
                count = 1
                pre_s = s[(index - 1) * unit : last_index]
            else:
                continue
            index += 1    
        result_list.append(len(result)) 
        unit += 1
    
    answer = min(result_list)
    
    return answer
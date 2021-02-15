def solution(s):
    answer = []
    
    s = s[1: -1]
    
    result = []
    s_list = s.split('},')
    s_list.sort(key = lambda x : len(x)) # 길이 순으로 정렬 
    
    for string in s_list:
        if string[-1] != '}':
            string = string[1:]
        else:
            string = string[1: -1]  
        
        s_list = string.split(',')
        
        for i in s_list:
            if int(i) not in result:
                result.append(int(i))
    #print(result)
    answer = result
    return answer
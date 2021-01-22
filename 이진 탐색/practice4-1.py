# bisect 이용한 경우 
from bisect import bisect_right, bisect_left 

def solution(words, queries):
    answer = []
    
    # 길이 별로 문자열을 저장하기 위해서 hashmap 이용 
    # ?가 접두사인 경우도 있을 수 있으므로 뒤집은 문자열도 저장 
    l_words = {}
    r_words = {} 
    for word in words:
        length = len(word)
        if length in l_words:
            l_words[length].append(word) 
            r_words[length].append(word[::-1]) # 뒤집은 문자열도 저장 
        else:
            l_words[length] = [word]
            r_words[length] = [word[::-1]]
    
    # 문자열 각각 정렬 
    for i in l_words:
        l_words[i].sort()
        r_words[i].sort()
            
    # print(l_words)
    # print(r_words)
    
    
    for query in queries:
        length = len(query)
        if length not in l_words: # 쿼리 길이에 해당하는 문자열이 없으면 검색 결과가 없는거니까 0
            answer.append(0)
            continue
        if query[0] == '?' and query[len(query) - 1] == '?': # 모두 ?인 경우, 해당 길이랑 같은 문자열 수만큼 
            answer.append(len(l_words[length]))
            continue
        if query[len(query) - 1] == '?': # 접미사인 경우, fraaa, frzzz 범위 안에 문자열이 있으면 되므로 replace를 이용해서 
            s_query = query.replace('?', 'a')
            e_query = query.replace('?', 'z')
            first_index = bisect_left(l_words[length], s_query)
            last_index = bisect_right(l_words[length], e_query)
            if first_index == None: # 쿼리랑 같은 길이의 문자열도 있는 경우 first_index == None이면 검색 결과가 없다는 의미이므로 
                answer.append(0)
            else:
                answer.append(last_index - first_index) # 범위 안에 해당하는 문자열이 있는 경우 갯수 구해서 추가 
            continue
        if query[0] == '?': # 접두사인 경우, ????o 인 경우 뒤집어서 o????로 만들고 ?를 각각 a, z로 변경 그리고 뒤집은 문자열로 이진탐색 
            r_query = query[::-1]
            s_query = r_query.replace('?', 'a')
            e_query = r_query.replace('?', 'z')
            first_index = bisect_left(r_words[length], s_query)
            last_index = bisect_right(r_words[length], e_query)
            if first_index == None:
                answer.append(0)
            else:
                answer.append(last_index - first_index)
            continue
            
        #print(s_query, e_query)
        #print(query, first_index, last_index)
        
        
    #print(result)
    #answer = result
    return answer
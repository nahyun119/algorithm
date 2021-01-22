# bisect 를 이용하지 않고 문제 풀면 이렇게 
def f_b_search(start, end, words, s, e): # query 범위 안에 해당하는 첫번째 인덱스 구하기 
    #print(start, end, words, s, e)
    if start > end: 
        return None
    mid = (start + end) // 2

    if (mid == 0 or words[mid - 1] < s) and (s <= words[mid] and words[mid] <= e):
         # mid == 0이거나 mid 이전이 쿼리 처음부분보다 작은 경우이면서 
         # words[mid] 가 범위 안에 있는 경우 
        return mid 
    if words[mid] < s: # 시작 부분보다 작으면 시작점 이동 
        return f_b_search(mid + 1, end, words, s, e)
    else: # 그렇지 않은 경우 s <= words[mid]인 경우 처음 인덱스를 구해야하니까 끝점을 이동 
        return f_b_search(start, mid - 1, words, s, e)

def l_b_search(start, end, words, s, e):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == len(words) - 1 or words[mid + 1] > e) and (s <= words[mid] and words[mid] <= e):
        # mid가 끝이면서 mid 다음 값이 쿼리 끝 범위보다 큰 경우이면서 범위 안에 해당하는 경우 
        return mid
    if words[mid] > e: # 끝 부분보다 큰 경우, 끝을 줄인다. 
        return l_b_search(start, mid - 1, words, s, e)
    # if words[mid] <= s: 
    #     return l_b_search(mid + 1, end, words, s, e)
    else: # words[mid] <= e인 경우 마지막 인덱스를 알기위해 시작점을 이동 
        return l_b_search(mid + 1, end, words, s, e)
    
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
            first_index = f_b_search(0, len(l_words[length]) - 1, l_words[length], s_query, e_query) 
            last_index = l_b_search(0, len(l_words[length]) - 1, l_words[length], s_query, e_query)
            if first_index == None: # 쿼리랑 같은 길이의 문자열도 있는 경우 first_index == None이면 검색 결과가 없다는 의미이므로 
                answer.append(0)
            else:
                answer.append(last_index - first_index + 1) # 범위 안에 해당하는 문자열이 있는 경우 갯수 구해서 추가 
            continue
        if query[0] == '?': # 접두사인 경우, ????o 인 경우 뒤집어서 o????로 만들고 ?를 각각 a, z로 변경 그리고 뒤집은 문자열로 이진탐색 
            r_query = query[::-1]
            s_query = r_query.replace('?', 'a')
            e_query = r_query.replace('?', 'z')
            first_index = f_b_search(0, len(r_words[length]) - 1, r_words[length], s_query, e_query)
            last_index = l_b_search(0, len(r_words[length]) - 1, r_words[length], s_query, e_query)
            if first_index == None:
                answer.append(0)
            else:
                answer.append(last_index - first_index + 1)
            continue
            
        #print(s_query, e_query)
        #print(query, first_index, last_index)
        
        
    #print(result)
    #answer = result
    return answer
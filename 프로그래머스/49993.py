def solution(skill, skill_trees):
    answer = 0
    
    k = list(skill)
    length = len(k)
    
    # 만약 없는 경우 -1이 나오는 경우 실제 해당 인덱스에다가 1000을 더해서 인덱스 배열에 넣는다.
    # 아무것도 일치하지 않는 경우에도 index를 더하기 때문에 오름차순으로 정렬될 것이고,
    # 있는 경우에도 인덱스가 들어가서 오름차순으로 정렬될 것이다.
    # 인덱스 배열이랑 인덱스 배열을 정렬한 것이랑 같으면 가능한 스킬 트리이므로 카운트한다. 

    for tree in skill_trees:
        indices = []
        for index, i in enumerate(k):
            c_index = tree.find(i)
            if c_index == -1:
                indices.append(index + 1000)
            else:
                indices.append(c_index)
        temp = indices[:]
        indices.sort()
        if temp == indices:
            answer += 1
        # if is_ok:
        #     answer += 1
        
        
    return answer
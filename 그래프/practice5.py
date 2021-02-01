# 원래 작년 순위 순서대로 먼저 데이터를 입력받고
# 그 순위대로 진입차수를 설정하였다. 1등이면 0, 2등이면 1, 3등이면 2 이런 식으로 앞에 사람들을 거쳐야 도달할 수 있다는 의미로
# 그런 후 작년과 상대적으로 순위가 달라진 쌍이 들어오면 
# 작년엔 이겼다가 올해 진 경우는 indegree += 1하고, 반대인 경우는 indegree -= 1을 하여 진입차수를 변경해서 순위를 다르게 하였다.
# 그러다가 위상정렬을 진행하는데 q가 빈 경우 cycle인 경우이므로 impossible 
# 순위대로 indegree이므로 중복이 없는데, q의 길이가 1이상인 경우 중복이므로 확실한 순위가 없다는 것을 의미해서 ?를 출력 



from collections import deque

result = []

def t_sort():
    global result 

    n = int(input())
    
    last_grade = [0] + list(map(int, input().split()))
    orgin_indegree = [0] * (n + 1)
    for i in range(1, n + 1):
        orgin_indegree[last_grade[i]] = i - 1

    indegree = orgin_indegree[:]
    # print(last_grade)
    # print(orgin_indegree)

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        #print(orgin_indegree[a], orgin_indegree[b])
        if orgin_indegree[a] > orgin_indegree[b]: # 원래 순서 확인, 원래 순서랑 상대적으로 반대 순위라는 것이므로 
            indegree[a] -= 1  # indegree 하나씩 증가 
            indegree[b] += 1
        elif orgin_indegree[a] < orgin_indegree[b]: # 원래 순서 확인 
            indegree[a] += 1
            indegree[b] -= 1


    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    

    re_list = []
    is_impossible = False
    is_certain = True
    for j in range(n): # 노드 수만큼 반복 
        #print(q)
        if len(q) == 0:
            is_impossible = True
            #result.append("IMPOSSIBLE")
            break 
        if len(q) >= 2: # q 크기가 1이 아니라면 진입차수가 동일하다는 것이 있다는 의미이므로 데이터 일관성 x 
            is_certain = False
            break
        node = q.popleft()
        re_list.append(node)
        for i in range(1, n + 1):
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    #print(is_impossible)
    if is_impossible:
        result.append("IMPOSSIBLE")
    elif not is_certain:
        result.append("?")
    else:
        result.append(re_list)
    #print(re_list)
    

    # print(orgin_indegree)
    # print(indegree)


def main():
    global result 

    T = int(input())

    for _ in range(T):
        t_sort()

    #print(result)
    for i in range(T):
        #print(type(result[i]))
        if str(type(result[i])) == "<class 'list'>":
            #print("hello")
            for r in result[i]:
                print(r, end = ' ')
            print()
        else:
            print(result[i])

if __name__ ==  "__main__":
    main()
T = int(input())
for t in range(T):
    n, m, k, A, B = map(int, input().split()) # 접수 창구 수, 정비 창구 수, 고객 수, 지갑 분실 접수, 지갑 분실 정비 
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_visited = [None] * n
    b_visited = [None] * m
    time = list(map(int, input().split()))
    a_waiting = []
    b_waiting = []

    a_people = 0
    use_list = [[0, 0] for _ in range(k + 1)] # 몇 번 창구 사용했는지 

    count = 0
    p_index = 1

    while time or a_people or b_waiting:
        while time and time[0] == count:
            time.pop(0)
            a_waiting.append(p_index)
            p_index += 1
        
        # 접수 창구 처리 
        for i in range(n):
            if a_visited[i]: # 손님있으면 
                a_visited[i][1] -= 1 # 시간 줄이기 
                if a_visited[i][1] == 0: # 시간 다되면 
                    b_waiting.append(a_visited[i][0]) # 정비 창구로 이동 
                    a_visited[i] = None 
                    a_people -= 1 # a에 있는 사람 감소 
        
            if not a_visited[i]: # 손님 없으면 
                if a_waiting:
                    idx = a_waiting.pop(0)
                    a_visited[i] = [idx, a[i]]
                    a_people += 1
                    use_list[idx] = [i + 1, 0]

        # 정비 창구 처리 
        for i in range(m):
            if b_visited[i]: # 손님있으면 
                b_visited[i][1] -= 1
                if b_visited[i][1] == 0:
                    b_visited[i] = None

            if not b_visited[i]:
                if b_waiting:
                    idx = b_waiting.pop(0)
                    b_visited[i] = [idx, b[i]]
                    use_list[idx] = [use_list[idx][0], i + 1]

        count += 1

    #print(use_list)

    total = 0
    for i in range(1, k + 1):
        if use_list[i] == [A, B]:
            total += i
    
    if total == 0:
        print('#{} {}'.format(t + 1, -1))
    else:
        #print(result)
        print('#{} {}'.format(t + 1, total))
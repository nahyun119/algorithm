# 우선 순위를 잘 파악하자ㅠ 

T = int(input())
for t in range(T):
    n, m, k, A, B = map(int, input().split()) # 접수 창구 수, 정비 창구 수, 고객 수, 지갑 분실 접수, 지갑 분실 정비 
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_visited = [0] * n
    b_visited = [0] * m
    time = list(map(int, input().split()))
    people = [[-1, 0, -1] for _ in range(k)] # 사람들 상태 -1: 접수 전, 0: 접수 대기, 1: 접수 중, 2: 정비 대기,  3: 정비 중, 4: 정비 후 

    use_list = [[0, 0] for _ in range(k)] # 몇 번 창구 사용했는지 

    visited = [0] * k
    count = 0

    while True:
        if 0 not in visited:
            break 
        
        t1 = []
        t2 = []

        for i in range(k): # 먼저 시간을 모두 줄이고 창구에서 뺀다. 
            if people[i][0] == -1 and time[i] <= count: # 접수 전에 시간이 되면 접수 준비로 변경 
                people[i] = [0, 0, 0, count]
            if people[i][0] == 0:
                t1.append((i, people[i]))
            if people[i][0] == 1:
                people[i][1] -= 1
                if people[i][1] == 0: # 다 된 경우 
                    a_visited[people[i][2]] = 0
                    people[i] = [2, 0, people[i][2], count] # 먼저 온 순서대로, 접수 창구 순서대로 정렬해야하므로 
            if people[i][0] == 2:
                t2.append((i, people[i]))
            if people[i][0] == 3:
                people[i][1] -= 1
                if people[i][1] == 0: # 다 된 경우 
                    b_visited[people[i][2]] = 0
                    people[i] = [4, 0, -1]
                    visited[i] = 1
            
        # 먼저 온 순서대로 
        # temp = [(i, people[i]) for i in range(k) if people[i][0] == 0] # 정비 전인 경우 
        t1.sort(key = lambda x : (x[1][3], x[1][2]))
        for te in t1:
            index, p = te
            for j in range(n):
                if a_visited[j] == 0:
                    a_visited[j] = index + 1
                    people[index][0] = 1
                    people[index][1] = a[j]
                    people[index][2] = j
                    use_list[index] = [j + 1, 0]
                    break 
                    

        # 접수 창구 번호 작은 순서대로 우선순위 부여                
        # temp = [(i, people[i]) for i in range(k) if people[i][0] == 2] # 정비 전인 경우 
        t2.sort(key = lambda x : (x[1][3], x[1][2]))

        for te in t2:
            index, p = te
            for j in range(m):
                if b_visited[j] == 0:
                    b_visited[j] = index + 1
                    people[index][0] = 3
                    people[index][1] = b[j]
                    people[index][2] = j
                    use_list[index] = [use_list[index][0], j + 1]
                    break
        count += 1

    total = 0
    for i in range(k):
        if use_list[i] == [A, B]:
            total += i + 1
    
    if total == 0:
        print('#{} {}'.format(t + 1, -1))
    else:
        #print(result)
        print('#{} {}'.format(t + 1, total))

                
                
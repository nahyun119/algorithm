# 끝나는 시간을 기준으로 정렬을 한다. 
# 만약 끝나는 시간이 같다면 시작하는 시간 순서대로 정렬을 한다.
# 그런 다음 하나씩 차례대로 돌면서 이미 선택한 시간의 끝나는 시간과 다음 시작 시간이랑 비교한 후
# 다음 시작 시간이 끝나는 시간 이후면 count하고 선택한 시간을 업데아트한다. 


def main():
    n = int(input())

    time = []
    for i in range(n):
        a, b = map(int, input().split())
        time.append((a, b))
    
    time.sort(key = lambda x : (x[1], x[0]))

    #print(time)
    count = 1
    start, end = time[0]
    for i in range(1, n): # 앞에서부터 천천히 탐색 
        n_start, n_end = time[i]
        if end <= n_start:
            #print(start, end, n_start, n_end)
            count += 1
            start = n_start
            end = n_end    
           

    print(count)


if __name__ ==  "__main__":
    main()
def solution(n):
    answer = 0
    
    total = 0
    for i in range(1, n + 1):
        if i + i + 1 > n: # 현재 숫자랑 다음 숫자 합이 n보다 크면 그 이후도 볼 필요없으므로 종료 
            break
        total = 0
        for j in range(i, n + 1):
            total += j
           # print(i, j, total)
            if total == n:
                answer += 1
                break
            elif total > n:
                break 
                
    answer += 1 # 자기자신
    return answer
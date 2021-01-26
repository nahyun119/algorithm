# An = min(An-1 + A1, An-2 + A2, An-3 + A3.... , An-i + Ai)
# 이 때, N - i >= i 일 때까지 
# 이렇게 점화식을 생각해서 풀었다.. 

import time

def main():

    start_time = time.time()
    N, M = map(int, input().split())
    dp = [-1] * 100001
    dp[0] = 0 # 0원은 화폐를 아무것도 사용안했을 때 만들 수 있다. 
    for i in range(N):
        dp[int(input())] = 1
    
    for i in range(1, M + 1):
        if dp[i] == 1: # 동전 하나로 만들 수 있으므로 패스 
            continue
        else:
            min_coin = 10001 # 화폐가치는 10001 아래이므로 최대 1원으로 10001개를 만들 수 있음 그래서 10001로 초기화 
            for j in range(1, i):
                #print(i, j, min_coin)
                if i - j < j:
                    break
                if dp[j] == -1: # 동전이 없는 경우 패스  
                    continue
                else:
                    value = dp[i - j] + dp[j]
                    if min_coin > value:
                        min_coin = value
            if min_coin != 10001:
                dp[i] = min_coin
    #print(dp)
    print(dp[M]) 
    end_time = time.time()
    print(end_time - start_time)
            


if __name__ ==  "__main__":
    main()
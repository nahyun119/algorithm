# An = min(An-1 + A1, An-2 + A2, An-3 + A3.... , An-i + Ai)
# 이 때, N - i >= i 일 때까지 
# 이렇게 점화식을 생각해서 풀었다.. 
# 근데 화폐 종류만 생각해서 진행해도 될 것 같아서 다시 수정 

# M이 작은 경우는 시간 차이가 크게 없었지만
# M을 10000으로 한 경우 
# example4.py처럼 모든 경우를 다 확인한 것보다 example4-1.py처럼 coin만 본 경우가
# 훨씬 빨랐다! 모든 경우를 확인할 필요는 없다
# 이미 이전 것들은 최소로 맞춘거라 거기서 coin 들을 더해서 해당 값을 만들 수 있는지 없는지를 판단하면 된다. 

import time
def main():
    start_time = time.time()

    N, M = map(int, input().split())
    dp = [10001] * (M + 1)
    dp[0] = 0 # 0원은 화폐를 아무것도 사용안했을 때 만들 수 있다. 

    coins = [0] # 0원도 포함 
    for i in range(N):
        coin = int(input())
        coins.append(coin)

    for coin in coins:
        if coin <= M:
            dp[coin] = 1 

    for i in range(1, M + 1):
        #print(dp)
        if dp[i] == 1: # 동전 하나로 만들 수 있으므로 패스 
            continue
        else:
            min_coin = 10001 # 화폐가치는 10001 아래이므로 최대 1원으로 10001개를 만들 수 있음 그래서 10001로 초기화 
            for coin in coins:
                if i - coin  >= 0 and i - coin <= M:
                    value = dp[i - coin] + dp[coin] # dp[coin]은 어차피 1 
                    if min_coin > value:
                        min_coin = value 
            if min_coin != 10001:
                dp[i] = min_coin
    #print(dp)
    if dp[M] == 10001:
        print(-1)
        return
    print(dp[M]) 

    end_time = time.time()
    print(end_time - start_time)
            


if __name__ ==  "__main__":
    main()
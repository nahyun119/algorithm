def main():
    N = int(input())

    counseling = [(0, 0)] * 16
    dp = [0] * 16

    for i in range(N):
        T, P = map(int, input().split())
        counseling[i] = (T,P)

    max_money = 0
    for i in range(N - 1, -1, -1):
        T, P = counseling[i] 
        #print(dp)
        if i + T <= N: # 시간 안에 끝낼 수 있으면
            dp[i] = max(dp[i + T] + P, max_money)
            max_money = dp[i]
        else:
            dp[i] = max_money

    # print(counseling)
    # print(dp)
    print(max(dp))

if __name__ ==  "__main__":
    main()
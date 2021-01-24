def main():
    N = int(input())

    foods = list(map(int, input().split()))

    dp = [0] * 101 # 식량 창고가 100개까지 있으므로

    dp[1] = foods[0] # a1 = a1
    dp[2] = foods[1] # a2 = a2
    dp[3] = dp[1] + foods[2] # a3 = a1 + a3 인게 최대이므로 

    for i in range(2, N):
        dp[i] = max(dp[i - 1], dp[i - 2] + foods[i]) # 이전 창고를 털었을 때의 양과 내 전전 창고를 턴 경우에 양 + 지금 내가 있는 위치 식량 양 중 
                                                     # 더 큰 애들을 넣는다. 
    
    # 3번째를 선택할 때까지 값은 위에 선언한 것처럼 동일하다.
    # 그리고 4번째부터는 자신 바로 전 애들을 빼고 나머지 N이면 0,1,,,, N - 2까지 중에서 최대 값이랑 자신이랑 더하면 된다. 
    # 그러면 항상 최대값을 유지할 수 있다. 
    for i in range(4, N + 1): # 내가 한 방법 
        part = dp[: i - 1]
        dp[i] = max(part) + foods[i - 1]

        

    print(dp[N])

     

if __name__ ==  "__main__":
    main()
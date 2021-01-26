def main():
    N = int(input())

    dp = [0] * 1001

    dp[1] = 1 # n = 1일 때 덮는 경우의 수 총 1개 
    dp[2] = 3 # n = 2일 때 덮는 경우의 수 총 3개 

    for i in range(3, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 796796
    
    print(dp[N])


                

    
    

if __name__ ==  "__main__":
    main()
def main():
    N = int(input())

    dp = [0] * N 
    dp[0] = 1
    
    index2 = 0
    index3 = 0
    index5 = 0

    # 인덱스말고 각 수를 곱한 수를 저장하는 변수도 선언 
    value2 = 2
    value3 = 3
    value5 = 5 

    for i in range(N - 1):
        
        dp[i] = min(value2, value3, value5)

        if dp[i] == value2:
            index2 += 1
            value2 = dp[index2] * 2
        if dp[i] == value3:
            index3 += 1
            value3 = dp[index3] * 3
        if dp[i] == value5:
            index5 += 1
            value5 = dp[index5] * 5
        
        
    print(dp[N - 1])



if __name__ ==  "__main__":
    main()
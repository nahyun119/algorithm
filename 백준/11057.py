def main():
    n = int(input())
    numbers = [1] * 9
    dp = [0] * (n + 1)
    if n == 1:
        print(10)
        return
    else:
        dp[1] = 10

    for i in range(2, n + 1):
        total = 0
        for j in range(9):
            total += numbers[j]
            numbers[j] = total
        dp[i] = dp[i - 1] + sum(numbers)
        #print(numbers)
        
    print(dp[n] % 10007)

if __name__ ==  "__main__":
    main()
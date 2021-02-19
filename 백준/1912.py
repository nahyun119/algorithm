import sys
input = sys.stdin.readline

def main():
    n = int(input())
    numbers = list(map(int, input().split()))

    dp = [0] * n
    dp[0] = numbers[0]

    for i in range(1, n):
        # 자기 자신이랑 이전 값이랑 자기 더한거랑 계속 더한 것 중에서 제일 큰 값 
        dp[i] = max(numbers[i], numbers[i] + numbers[i - 1], dp[i - 1] + numbers[i])
    
    print(max(dp))

if __name__ ==  "__main__":
    main()
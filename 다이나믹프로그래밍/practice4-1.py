# 가장 긴 증가하는 부분 수열 LIS 문제
# 내림차순이므로 가장 긴 감소하는 부분 수열 문제로 원소를 뒤집어서 진행하면 된다.
# LIS 점화식: D[i] = max(D[i], D[j] + 1) 0 <= j < i, if array[j] < array[i] - >외우기 

def main():
    N = int(input())

    soldier = list(map(int, input().split()))

    soldier.reverse() # 내림차순이므로 뒤집는다. 

    dp = [1] * (N + 1) # 길이니까 1로 초기화 자기 자신일 수 있으므로  

    for i in range(1, N):
        for j in range(0, i):
            if soldier[j] < soldier[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    length = max(dp)

    print(N - length)

if __name__ ==  "__main__":
    main()
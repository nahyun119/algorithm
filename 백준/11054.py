import sys
input = sys.stdin.readline
def main():
    n = int(input())
    numbers = list(map(int, input().split()))


    def lis():
        dp = [1] * (n)
        for i in range(n):
            for j in range(i):
                if numbers[j] < numbers[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp 

    def lcs():
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if numbers[j] > numbers[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp 

    dp_1 = lis()
    dp_2 = lcs()

    max_dp1 = max(dp_1)
    max_dp2 = max(dp_2)
    print(max_dp1)
    print(max_dp2)

    max_idx1 = dp_1.index(max_dp1)
    max_idx2 = dp_2.index(max_dp2)
    lis_list = []
    lcs_list = []

    while max_idx1 >= 0:
        if dp_1[max_idx1] == max_dp1:
            lis_list.append(numbers[max_idx1])
            max_dp1 -= 1
        max_idx1 -= 1

    while max_idx2 >= 0:
        if dp_2[max_idx2] == max_dp2:
            lcs_list.append(numbers[max_idx2])
            max_dp2 -= 1
        max_idx2 -= 1

    lis_list.reverse()
    lcs_list.reverse()

    print(*lis_list)
    print(*lcs_list)
if __name__ ==  "__main__":
    main()
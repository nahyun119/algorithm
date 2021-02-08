import sys
input = sys.stdin.readline


# dp는 역시 어렵다,,
# 대각선으로 비교한 후, n 열에서 n - 1열에서 선택하지 않고 , n - 2열에서 선택한 경우에도 고려해야한다. -> 이걸 어떻게 해야할지 감이 잡히지 않았는데
# 행을 더 늘려서 첫번째 행에 n -2 열의 최댓값을 넣어서 비교해서 넣을 수 있도록 하면 된다. 

result = []
def solve():
    n = int(input())
    dp = [[0] * n]
    for i in range(2):
        dp.append(list(map(int, input().split())))
    #print(dp)
    dp[0][1] = max(dp[1][0], dp[2][0])
    for i in range(1, n):
        dp[1][i] = max(dp[2][i - 1] + dp[1][i], dp[1][i] + dp[0][i - 1])
        dp[2][i] = max(dp[2][i] + dp[1][i - 1], dp[2][i] + dp[0][i - 1])

        if i < n - 1: 
            dp[0][i + 1] = max(dp[2][i], dp[1][i])
    
    #print(dp)
    #print(max(dp[1][n - 1], dp[2][n - 1]))
    result.append(max(dp[1][n - 1], dp[2][n - 1]))


def main():
    global result 
    T = int(input())

    for i in range(T):
        solve()

    for re in result:
        print(re)

if __name__ ==  "__main__":
    main()
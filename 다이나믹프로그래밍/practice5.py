# 2를 곱하는 index, 3을 곱하는 index, 5를 곱하는 index 를 각각 선언
# 그래서 각 index에 해당하는 값에 2, 3, 5를 맞게 곱한 후 
# 거기 중 최솟값을 dp 에 추가하도록 한다. 

# 근데 2,3,5를 곱할 때 겹치는 수가 있다면
# index를 늘려서 다음 값을 가져오도록 한다. 

def main():
    N = int(input())

    dp = [1]
    
    index2 = 0
    index3 = 0
    index5 = 0

    for i in range(N - 1):
        # print(dp)
        value2 = dp[index2] * 2
        if value2 in dp:
            index2 += 1
            value2 = dp[index2] * 2
        value3 = dp[index3] * 3
        if value3 in dp:
            index3 += 1
            value3 = dp[index3] * 3
        value5 = dp[index5] * 5
        if value5 in dp:
            index5 += 1
            value5 = dp[index5] * 5

        min_value = min(value2, value3, value5)

        if value2 == min_value:
            dp.append(min_value)
            index2 += 1
        elif value3 == min_value:
            dp.append(min_value)
            index3 += 1
        elif value5 == min_value:
            dp.append(min_value)
            index5 += 1
        
    print(dp[N - 1])



if __name__ ==  "__main__":
    main()
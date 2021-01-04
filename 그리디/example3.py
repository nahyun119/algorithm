## 1이 될 때까지 최소한의 횟수로 연산을 하는 경우이므로
## 빼는 것보다는 최대한 많이 나누는 것이 중요하다. 

## K가 2 이상이라면 1을 빼는 것보다 훨씬 빨리 N을 감소시킬 수 있다. -> 그리디 방법을 이용해서 최적의 해를 구할 수 있는 이유 

def main():
    N, K = map(int, input().split())
    
    # count = 0

    # while True:
    #     print(N)
    #     if(N <= 1):
    #         break
    #     if(N % K == 0):
    #         N = int(N / K)
    #         count += 1
    #     else :
    #         N -= 1
    #         count += 1

    # print(count) 

    # 근데 복잡도를 고려했을 때, N < K 인 경우처럼 N을 나누지 못하고 일일이 빼야하는 경우
    # N이 100억 이상이면 굉장히 오래걸린다. 따라서 나눌 수 있는 경우랑 아닌 경우 값을 구해서 계산하는 것도 있다. 

    result = 0
    
    while True:
        target = (N // K) * K
        result += (N - target)

        print(N, target, result)

        N = target 
        if N < K:
            break
        result += 1
        N = N // K

    result += (N - 1)    
    print(result)

if __name__ ==  "__main__":
    main()  
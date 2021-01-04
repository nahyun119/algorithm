## 아니면 그냥 간단하게 가장 큰 수 더하는 횟수 m / (k+1) * k 구하고 
## m - 가장 큰 수 더하는 횟수를 구해서 두번째로 큰 수에 곱해서 더하는 경우도 있다. 

def main():
    ## 각각 값 입력받기 
    N, M, K = map(int, input().split())

    ## 리스트 입력받기 
    num_list = list(map(int, input().split()))

    sorted_list = sorted(num_list)
    first_value = sorted_list[N - 1]
    second_value = sorted_list[N - 2]

    # 가장 큰 수를 k번 반복하고 두번째로 큰 수를 하나를 추가한 패턴 만들기 
    pattern = []
    for value in range(K):
        pattern.append(first_value)

    pattern.append(second_value)

    result = 0

    ## 패턴을 circular 하게 더할 수 있도록 M번 반복해서 더할 수 있도록 
    for value in range(M):
        result += pattern[value % (K + 1)]    
    
    print(result)

if __name__ ==  "__main__":
    main()   
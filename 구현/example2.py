def main():
    N = int(input())


    hour_count  = 0

    ## 한 시간에 3이 들어가는 시간 횟수 구하기 
    for i in range(60):
        for j in range(60):
            if(i % 10 == 3 or i // 10 == 3):
                hour_count += 1
            else:
                if(j % 10 == 3 or j // 10 == 3):
                    hour_count += 1
    
    result = 0

    # 시에 3이 포함되는 경우는 3600을 더하고, 아닌 경우는 한 시간에 3이 들어가는 횟수 더하기 
    for value in range(N + 1):
        if(value % 10 == 3):
            result += 3600
        else:
            result += hour_count
        
    print(result)


    # 아니면 24 * 60 * 60 이 모든 경우의 수이기 때문에 3중 반복문을 해서 
    # if '3' in str(i) + str(j) + str(k):
    # 이를 이용해서 확인해도 된다. 

if __name__ ==  "__main__":
    main()    
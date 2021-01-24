def main():
    X = int(input())

    dp_tbl = [0] * 30001  # 1에서부터 30000까지 이므로 dp table 생성
    
    for i in range(2, X + 1):
        dp_tbl[i] = dp_tbl[i - 1] + 1 # 1을 빼는 경우
        if i % 2 == 0: # 2로 나누어 떨어지는 경우
            dp_tbl[i] = min(dp_tbl[i], dp_tbl[(i // 2)] + 1)
        if i % 3 == 0: # 3으로 나누어 떨어지는 경우
            dp_tbl[i] = min(dp_tbl[i], dp_tbl[(i // 3)] + 1)
        if i % 5 == 0: # 5로 나누어 떨어지는 경우 
            dp_tbl[i] = min(dp_tbl[i], dp_tbl[(i // 5)] + 1)


    print(dp_tbl[X])            
    




if __name__ ==  "__main__":
    main()
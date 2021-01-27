def main():
    a = list(str(input()))
    b = list(str(input()))

    # b가 항상 더 길이가 긴 문자열이 되도록 
    if len(a) > len(b):
        temp = a[:]
        a = b[:]
        b = temp[:]

    rm_number = len(b) - len(a) # 뺄 수 있는 기회 
    last_index = 0

    dp = [0] * (len(a))

    # 일단 비교해서 서로 다르고 뺄 수 있다면 같은 문자가 나올 때까지 뺄 수 있는 기회만큼 뺀다
    # 그리고 다 빼면 그 다음부터 다른 문자라면 교체만 할 수 있도록 한다.
    # 근데 이렇게하면 일부는 맞고 일부는 틀린 결과가 나온다.
    # 또한 DP 가 아닌 것 같다.. 그냥 구현한거 같다 ㅠ 
    for i in range(len(a)):
        #print(dp, b[last_index], a[i])
        if a[i] != b[last_index]:
            if rm_number != 0:
                for j in range(i, len(b)):
                    #print(rm_number, a[i], b[last_index])
                    if rm_number == 0:
                        last_index = j
                        break 
                    if a[i] == b[j]:
                        break
                    rm_number -= 1
                    dp[i] += 1
            else:
                dp[i] = dp[i - 1] + 1 # 못 빼니까 교체 
        last_index += 1
    

    
    print(max(dp))

                    





if __name__ ==  "__main__":
    main()
# practice 3 다시 코딩해본거 

def main():
    s = str(input())
    
    count = 0

    # 0이 더 많은 경우 
    if s.count('0') > s.count('1'):
        for index in range(len(s) - 1):
            # 1이고 그 다음이 0이라면 연속된 숫자를 다 바꾼 것이기 때문에 count 
            if(s[index] == '1' and s[index] != s[index + 1]):
                count += 1
        # 마지막 요소 하나가 다른 경우         
        if s[len(s) - 1] == '1':
            count += 1       
    else:
        for index in range(len(s) - 1):
            # 0이고 그 다음이 1이라면 연속된 숫자를 다 바꾼 것이기 때문에 count 
            if(s[index] == '0' and s[index] != s[index + 1]):
                count += 1
        if s[len(s) - 1] == '0':
            count += 1         

    print(count)                


if __name__ ==  "__main__":
    main()  
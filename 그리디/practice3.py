def main():
    s = str(input())
    
    count = 0

    # 0이 더 많은 경우 
    if s.count('0') > s.count('1'):
        for index, value in enumerate(s):
            print(index, value)
            # 1이고 그 다음이 0이라면 연속된 숫자를 다 바꾼 것이기 때문에 count 
            if(value == '1'):
                if(index != len(s) - 1 and s[index + 1] != value):
                    count += 1
                if(index == len(s) - 1):
                    count += 1
            # if(value == '1' and s[index + 1] != value):
            #     count += 1
    else:
        for index, value in enumerate(s):
            print(index, value)
            # 0이고 그 다음이 1이라면 연속된 숫자를 다 바꾼 것이기 때문에 count 
            if(value == '0'):
                # 마지막 인덱스가 아니면서 다음 값이랑 다른 경우 count + 1
                if(index != len(s) - 1 and s[index + 1] != value):
                    count += 1
                # 마지막 인덱스인 경우 마지막 값을 뒤집어야하므로 count + 1    
                if(index == len(s) - 1):
                    count += 1   
            # if(value == '1' and s[index + 1] != value):
            #     count += 1


    print(count)                


if __name__ ==  "__main__":
    main()  
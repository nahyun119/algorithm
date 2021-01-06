# 문자열에서 0이거나 1이면 더하고 나머지는 다 더하도록 
# 곱하기를 해야 수를 더 크게 만들 수 있으므로 

# 0인 경우뿐만 아니라 1인 경우도 더하는 것이 좋다. 

def main():
    num_str = str(input())
    
    result = 0 

    for index, value in enumerate(num_str):
        if(index == 0):
            result = int(value)
        else:
            if(int(value) <= 1 or result <= 1):
                result = result + int(value)
            else:
                result = result * int(value)

    print(result)


if __name__ ==  "__main__":
    main()   
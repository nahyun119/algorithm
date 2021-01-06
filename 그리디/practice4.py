def check_num(value, s):
    i, j = 0, len(s) - 1
    
    while i < j:
        sum_value = s[i] + s[j]
        if(sum_value == value):
            return True
        elif sum_value < value:
            i += 1
        else :
            j -= 1

    return False

def main():
    N = int(input())
    coin_list = list(map(int, input().split()))

    sum_coin = sum(coin_list)

    coin_list.sort()


    for value in range(1, sum_coin + 1):
        if value in coin_list:
            continue
        else:
            if check_num(value, coin_list):
                continue
            else:
                print(value)
                break


if __name__ ==  "__main__":
    main()   
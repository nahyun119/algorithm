def main():
    n = int(input())
    length = len(list(str(n))) # 자리수 
    
    answer = 0
    for i in range(1, length):
        answer += 9 * (10 ** (i - 1)) * i
    
    number = 10 ** (length - 1)
    
    answer += ((n - number) + 1) * length

    print(answer)


if __name__ ==  "__main__":
    main()
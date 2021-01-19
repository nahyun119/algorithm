def main():
    num = list(map(int, input().split()))

    for i in range(1, len(num)):
        for j in range(i, 0, -1) : # i에서부터 0까지 -1 감소하여 이동
            if num[j] < num[j - 1]:
                num[j], num[j - 1] = num[j - 1], num[j]
                #num[j], num[j - 1] = num[j - 1], num[j]
            else: # 자기보다 작은 숫자 만나면
                break
        print(num)

if __name__ ==  "__main__":
    main()  
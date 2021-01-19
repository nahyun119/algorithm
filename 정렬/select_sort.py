def main():
    num = list(map(int, input().split()))

    for i in range(len(num)):
        min_num = i
        for j in range(i, len(num)):
            if num[min_num] > num[j]:
                    min_num = j
        num[i], num[min_num] = num[min_num], num[i]
        print(num)

    print(num)
if __name__ ==  "__main__":
    main()  
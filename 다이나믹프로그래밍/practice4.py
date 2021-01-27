def main():
    N = int(input())

    soldier = list(map(int, input().split()))

    dp = [soldier[0]]

    for i in range(1, N):
        #print(dp)
        min_value = min(dp)
        if soldier[i] > min_value:
            dp[-1] = soldier[i]
        elif soldier[i] < min_value:
            dp.append(soldier[i])
        
    #print(dp)
    print(N - len(dp))
if __name__ ==  "__main__":
    main()
def main():
    n, k = map(int, input().split())

    coins = []
    for _ in range(n):
        coins.append(int(input()))

    count = 0

    for i in range(n - 1, -1, -1): # 뒤에서부터 차례대로 하면 동전 수만큼 탐색해도 된다. 
        #print(i, k) 
        if coins[i] <= k: # 동전이랑 같은 가격이랑 같은 경우도 포함 
            coin = coins[i]
            num = k // coin # 동전 갯수 
            k = k - coin * num
            count += num
            #print(i, k, coin, count)
        if k <= 0:
            print(count)
            break

                

if __name__ ==  "__main__":
    main()
## coin type이 k개인 경우 
## 해당 코드의 시간복잡도는 O(k)

def main():
    n = 1260
    count = 0
    
    # coin types는 최소 동전으로 거슬러 주는 경우, 돈이 큰 순서대로 정렬하도록 
    coin_types = [500, 100, 50, 10]

    for value in coin_types:
        # 값을 coin으로 나누어서 나오는 몫 
        count += n // value

        # 나눠서 나온 나머지로 갱신 
        n = n % value
    
    print(count)

if __name__ ==  "__main__":
    main()    
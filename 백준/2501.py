def main():
    n, k = map(int, input().split())

    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    
    if len(result) < k:
        print(0)
    else:
        result.sort()
        print(result[k - 1])
    

if __name__ ==  "__main__":
    main()
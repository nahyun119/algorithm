def solve():
    test = list(map(int, input().split()))
    count = 1

    while True:
        #print(test, count)
        first = test[0]
        test = test[1:] 
        first -= count
        if first <= 0:
            test.append(0)
            #print(test)
            break
        test.append(first)
        count += 1
        if count > 5:
            count = 1
    
    return test

def main():
    for i in range(1):
        test = int(input())
        result = solve()
        print("#" + str(test), *result)


if __name__ ==  "__main__":
    main()
def solve():
    search = input().strip()
    string = input().strip()
    n = len(search)
    m = len(string)
    
    count = 0 
    for i in range(m):
        if i + n - 1 < m:
            temp = string[i: i + n]
            if temp == search:
                count += 1
    #print(count)

    return count


def main():
    for i in range(1):
        n = int(input())
        result = solve()
        print("#" + str(i + 1), result)

if __name__ ==  "__main__":
    main()
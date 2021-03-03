def solve():
    n = int(input())
    farm = []
    for _ in range(n):
        farm.append(list(input().strip()))
    
    total = 0

    mid = n // 2
    for i in range(n):
        width = mid - abs(i - mid)
        total += int(farm[i][mid])
        for j in range(1, width + 1):
            total += int(farm[i][mid + j])
            total += int(farm[i][mid - j])
    
    return total

def main():
    T = int(input())
    for i in range(T):
        result = solve()
        print("#" + str(i + 1), result)


if __name__ ==  "__main__":
    main()
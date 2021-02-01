def main():
    n = int(input())

    wait = list(map(int, input().split()))

    wait.sort()

    total_time = wait[0]
    result = wait[0]

    for i in range(1, n):
        total_time += wait[i]
        result += total_time

    print(result)
    
if __name__ ==  "__main__":
    main()
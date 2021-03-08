def solve():
    n, m = map(int, input().split())
    result = []
    def multi(value, step):
        #print(value, step)
        if step >= m:
            result.append(value)
            #print(result)
            return 
        
        multi(value * n, step + 1)


    multi(n, 1)
    return result[0]

def main():
    for i in range(1):
        n = int(input())
        result = solve()
        print("#" + str(i + 1), result)

if __name__ ==  "__main__":
    main()
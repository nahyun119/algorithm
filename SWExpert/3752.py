import itertools 

def solve():
    n = int(input())
    avail = set()
    grade = list(map(int, input().split()))
    
    for i in range(n):
        if i == 0:
            avail.add(0)
            avail.add(grade[i])
        else:
            result = set()
            for a in avail:
                result.add(a + grade[i])
                result.add(a)
            avail = result

    
    return len(avail)

def main():
    T = int(input())
    for i in range(T):
        result = solve()
        print("#" + str(i + 1), result)

if __name__ ==  "__main__":
    main()
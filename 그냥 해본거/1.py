import sys

def check(N, num):
    if num >= N:
        print(0)
        return

    d, q = divmod(num, 10)
    sum = q
    while d >= 10: # 나머지가 10일 때까지 
        d, q = divmod(d, 10)
        #print(d, q)
        sum += q
    sum += d

    if sum + num == N:
        print(num)
        return 
        
    check(N, num + 1)

def main():
    sys.setrecursionlimit(10**6)
    N = int(input())

    check(N, 0)

    #print(number)


if __name__ ==  "__main__":
    main()
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    costs = list(map(int, input().split()))
    costs = [0] + costs    
    #print(costs)

    for i in range(1, n + 1):
        costs[i] = max(costs[i], costs[1] * i) # 1개로 여러개 사는 경우
        for j in range(1, i // 2 + 1):
            #print(costs[i],  costs[i - j] + costs[j])
            costs[i] = max(costs[i],  costs[i - j] + costs[j])
           # print(i, j)
    
    print(costs[n])


if __name__ ==  "__main__":
    main()
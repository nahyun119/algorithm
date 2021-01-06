# 그리디 문제로 동전을 순서대로 오름차순 정렬을 한다.
# 그 후에 동전을 순서대로 합을 구한다.
# 만약에 1, 2, 4, 8인 경우 target = 1로 초기화
# 1 가능, 이 후 target + 1 =  2도 가능 
# 그리고 target + 2 해서 4도 가능 이 때 4까지 가능하므로 3도 가능하다는 것을 의미한다. 
# 오름차순으로 정렬된 동전들의 합에 다가 그 다음 순서의 동전을 합한 숫자만큼 동전 조합이 가능하다는 의미이다. 

def main():
    N = int(input())
    coin_list = list(map(int, input().split()))

    coin_list.sort()

    target = 1

    for value in coin_list:
        if target < value:
            break
        target += value 

    print(target)         


if __name__ ==  "__main__":
    main()   
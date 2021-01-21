# 이진 탐색이 아닌 계수 정렬을 이용한 풀이

def main():
    N  = int(input())
    products = list(map(int, input().split()))

    M = int(input())
    needs = list(map(int, input().split()))

    # 가능한 범위에서 몇 개가 있는지 저장하는 작업 
    num_list = [0] * 1000001
    for value in products: # 아니면 리스트 데이터를 받을 때 정할 수 있다. 
        num_list[value] += 1

    for value in needs:
        if num_list[value] != 0:
            print("Yes", end = ' ')
        else:
            print("No", end = ' ')
    


if __name__ ==  "__main__":
    main() 
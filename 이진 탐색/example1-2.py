# 집합 자료형을 이용한 경우 
def main():
    N  = int(input())
    products = set(map(int, input().split()))

    M = int(input())
    needs = list(map(int, input().split()))


    for value in needs:
        if value in products:
            print("Yes", end = ' ')
        else:
            print("No", end = ' ')
            
if __name__ ==  "__main__":
    main() 
# 안테나 위치부터 다른 집까지의 거리가 최소가 되어야하는데,
# 거리의 합이 최소가 될 수 있는 경우는 
# 집 중에서 중간 값에 설치를 해야 안테나와 다른 집들까지의 거리의 합이 최소가 된다.
# 따라서 입력받은 집 값을 정렬한 후 중간 값을 가져오면 된다. 

def main():
    N = int(input())
    houses = list(map(int, input().split()))

    houses.sort()

    answer = (N - 1) // 2
    
    print(houses[answer])
        
        

if __name__ ==  "__main__":
    main() 
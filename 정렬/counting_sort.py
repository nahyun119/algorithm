def main():
    num = list(map(int, input().split()))
    # 모든 원소의 값이 양의 정수라 가정, 즉 0보다 크거나 같다고 가정 
    counting = [0] * (max(num) + 1)

    for value in num: # 데이터 갯수 만큼 반복 
        counting[value] += 1
    
    for index in range(len(counting)): # 데이터 최대 값 크기 만큼 반복 
        for value in range(counting[index]):
            print(index, end = ' ')
    

if __name__ ==  "__main__":
    main() 
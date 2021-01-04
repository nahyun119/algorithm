## 입력 받은 리스트에서 각 행마다 제일 작은 수를 찾는다
## 제일 작은 수로 뽑힌 애들 중에서 가장 큰 수를 찾으면 된다. 

def main():
    N, M = map(int, input().split())
    
    
    for i in range(N):
        #print(i)
        num_list = list(map(int, input().split()))
        if(i == 0):
            min_value = min(num_list)
        else:
            if(min_value < min(num_list)):
                min_value = min(num_list)
    print(min_value)

if __name__ ==  "__main__":
    main()   
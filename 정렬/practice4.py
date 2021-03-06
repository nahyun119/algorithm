# 항상 작은 두 묶음을 더하는 것이 좋다. 
# 이렇게 하면 시간초과가 발생한다. 
# 그러므로 우선순위 큐를 사용하여 항상 순서대로 정렬되도록 하는 것이 좋다 -> practice4-1.py

def main():
    N = int(input())

    number_list = []

    for i in range(N):
        number_list.append(int(input()))

    if N <= 1:
        print(number_list[0])
        return 

    number_list.sort() # 오름차순 정렬

    while True:
       #print(number_list)
        length = len(number_list)
        total_list = []
        if length == 1: # 다 더해서 하나만 남은 경우
            break

        total = number_list[0] + number_list[1]
        total_list.append(total)
        total_list += number_list[2:]

        number_list = sorted(total_list)


    print(number_list[0])
 

        
if __name__ ==  "__main__":
    main() 
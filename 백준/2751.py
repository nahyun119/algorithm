import sys
input = sys.stdin.readline

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    
    pivot = numbers[0] # 맨 처음 원소를 pivot으로 
    num_list = numbers[1:] # 나머지 원소들은 list

    # left_side = 
    # right_side = 

    return quick_sort([x for x in num_list if x <= pivot]) + [pivot] + quick_sort([x for x in num_list if x > pivot])

def main():
    n = int(input())
    
    number_list = []
    for _ in range(n):
        number_list.append(int(input()))

    numbers = quick_sort(number_list)
    for number in numbers:
        print(number)



if __name__ ==  "__main__":
    main()
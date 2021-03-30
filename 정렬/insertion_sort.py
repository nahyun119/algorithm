numbers = list(map(int, input().split()))

for i in range(1, len(numbers)):
    for j in range(i, 0, -1):
        if numbers[j - 1] > numbers[j]:
            numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
        else: # 앞에는 이미 정렬되어 있으므로 비교했을 때 더 크면 그 앞에 있는 것들 보다도 크다는 의미이므로 break 
            break 
        # print(numbers)

print(numbers)

numbers = list(map(int, input().split()))
for i in range(len(numbers)):
    standard = i
    for j in range(i + 1, len(numbers)): # i + 1부터 마지막까지 중에서 제일 최솟값을 가져온 후 swap
        if numbers[standard] > numbers[j]:
            standard = j
    numbers[standard], numbers[i] = numbers[i], numbers[standard]
    print(numbers) 
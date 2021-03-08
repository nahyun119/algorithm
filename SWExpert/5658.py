T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    m = n // 4
    numbers = list(input().strip())
    original = numbers[:]

    avail = set()

    for i in range(0, n, m):
        temp = ''
        for j in range(m):
            temp += numbers[i + j]
        avail.add(temp)

    count = 0
    while True:
        numbers = [numbers[-1]] + numbers[: n - 1]
        if numbers == original:
            break 
        for j in range(0, n, m):
            temp = ''
            for u in range(m):
                temp += numbers[j + u]
            avail.add(temp)
        count += 1

    a = list(avail)
    a.sort(reverse = True)
    
    result = int(a[k - 1], 16)
    print("#" + str(t + 1), result)
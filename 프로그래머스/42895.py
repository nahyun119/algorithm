def solution(N, number):
    answer = 0

    numbers = []
    
    if N == number:
        return 1

    numbers.append(set([N]))
    
    for i in range(2, 9):
        temp = set()
        temp.add(int(str(N) * i))
        
        for j in range(i - 1):
            for x in numbers[j]:
                for k in numbers[-j - 1]:
                    temp.add(x + k)
                    temp.add(x * k)
                    temp.add(x - k)
                    temp.add(k - x)
                    if x != 0:
                        temp.add(k // x)
                    if k != 0:
                        temp.add(x // k)
                        
        if number in temp:
            return i
        numbers.append(temp)
        
    return -1
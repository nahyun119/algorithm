def solve():
    puzzle = []
    for i in range(9):
        puzzle.append((list(map(int, input().split()))))

    def check(numbers):
        for i in range(1, 10):
            if numbers.count(i) != 1:
                return False 
        return True

    x = 0
    y = 0

    for i in range(9):
        if not check(puzzle[i]):
            return 0
        if not check([puzzle[x][i] for x in range(9)]):
            return 0
        temp = []
        for j in range(3):
            temp += puzzle[x + j][y : y + 3]
        #print(temp)
        if not check(temp):
            return 0
        
        if y == 6:
            x += 3
            y = 0
        else:
            y += 3

    return 1

def main():
    T = int(input())
    for i in range(T):
        result = solve()
        print("#" + str(i + 1), result)

if __name__ ==  "__main__":
    main()

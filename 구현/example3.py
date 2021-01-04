# 입력이 a1 이 아니라 1a 이런 식으로 들어올 수 있으므로 예외처리를 해야한다


def transform(col):
    if col == 'a':
        return 1
    if col == 'b':
        return 2
    if col == 'c':
        return 3
    if col == 'd':
        return 4
    if col == 'e':
        return 5
    if col == 'f':
        return 6
    if col == 'g':
        return 7
    if col == 'h':
        return 8

def main():
    N = str(input())

    col = int(transform(N[0]))
    row = int(N[1])

    count = 0 

    # 파이썬의 ord 함수는 문자의 아스키 코드 값을 알려준다. 
    # a = 1 이라면 int(ord(N[0])) - int(ord('a')) + 1 
    # 이렇게 쉽게 문자를 숫자로 변경할 수 있다. 

    row_type = [2, 2, -2, -2, 1, -1, 1, -1]
    col_type = [-1, 1, -1, 1, 2, 2, -2, -2]

    for i in range(8):
        if (row + row_type[i] <= 8 and row + row_type[i] >= 1) and (col + col_type[i] <= 8 and col + col_type[i] >= 1):
            count += 1

    print(count)

if __name__ ==  "__main__":
    main()    
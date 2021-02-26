def solve():
    array = []
    for _ in range(100):
        array.append(list(map(int, input().split())))
    
    row_sum = 0
    col_sum = 0
    inter_sum1 = 0
    inter_sum2 = 0
    for i in range(100):
        rs = sum(array[i])
        row_sum = max(rs, row_sum)
        cs = sum([x[i] for x in array])
        col_sum = max(cs, col_sum)
        inter_sum1 += array[i][i]
        inter_sum2 += array[i][99 - i]
    
    return max(row_sum, col_sum, inter_sum1, inter_sum2)

def main():
    for i in range(10):
        t = int(input())
        result= solve()
        print("#" + str(t), result)

if __name__ ==  "__main__":
    main()
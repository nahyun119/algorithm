def check1(string, n): #길이가 짝수인 경우 
    front = string[:n//2]
    back = string[n // 2 :]
    back.reverse()
    for i in range(len(front)):
        if back[i] != front[i]:
            return False
    return True

def check2(string, n): # 길이가 홀수인 경우 
    #print(string)
    mid = n // 2
    #print(mid)
    for i in range(1, mid + 1):
        #print(string[mid - i], string[mid + i])
        if string[mid - i] != string[mid + i]:
            return False 
    return True 


def solve():
    n = int(input())
    is_even = False

    if n % 2 == 0:
        is_even = True
    
    graph = []
    for _ in range(8):
        graph.append(list(input().strip()))

    #count = 0
    
    
    result = []

    for i in range(8):
        for j in range(8):
            row = []
            col = []
            if i + n - 1 < 8:
                col = [graph[x][j] for x in range(i, i + n)]
                s_col = "".join(col)
                #if s_col not in result:
                if is_even: # 짝수라면 
                    if check1(col, n):
                            #count += 1
                        result.append(s_col)
                else:
                    if check2(col, n):
                            #count += 1
                        result.append(s_col)

            if j + n - 1 < 8:
                row = graph[i][j : j + n]
                s_row = "".join(row)
                #if s_row not in result:
                if is_even:
                    if check1(row, n):
                            #count += 1
                        result.append(s_row)
                else:
                    if check2(row, n):
                            #count += 1
                        result.append(s_row)
            #print(row, col)
    #print(result)
    return len(result)
                    
def main():
    for i in range(10):
        result = solve()
        print("#" + str(i + 1), result)



if __name__ ==  "__main__":
    main()
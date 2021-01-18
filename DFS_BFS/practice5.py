min = 1000000000
max = -1000000000

def dfs(num, index, n_list, a, s, m, d):
    global min, max
    if (a == 0 and s == 0 and m == 0 and d == 0) or index >= len(n_list) : # 연산을 모두 다한경우 
        #print("end")
        #result.append(num)
        if min > num:
            min = num
        if max < num:
            max = num
        return

    new_num = n_list[index]
    if a > 0: 
        dfs(num + new_num, index + 1, n_list, a - 1, s, m, d)
    if s > 0:
        # new_num = queue.popleft()
        dfs(num - new_num, index + 1, n_list, a, s - 1, m, d)
    if m > 0:
        dfs(num * new_num, index + 1, n_list, a, s, m - 1, d)
    if d > 0:
        # if num < 0: # 음수인 경우 
        #     d = ( -1 * num ) // new_num
        #     dfs( -1 * d, index+ 1, n_list, a, s, m, d - 1)
        # else:
        #     dfs(num // new_num, index+1, n_list, a, s, m, d -1)
        dfs(int(num / new_num), index+1, n_list, a, s, m, d -1) # 나눗셈 그냥 이렇게 하면 된다. 
        

def main():
    N  = int(input())
    number_list = list(map(int, input().split()))
    operator = list(map(int, input().split()))

    #print(N, number_list, operator)

    global min, max
    
    dfs(number_list[0], 1, number_list, operator[0], operator[1], operator[2], operator[3])
    
    print(max)
    print(min)

if __name__ ==  "__main__":
    main()
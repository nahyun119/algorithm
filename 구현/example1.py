def check(x, N):
    if(x < 1 or x > N):
        return False 
    else: 
        return True

def main():
    N = int(input())
    route = list(input().split())

    init_x = 1
    init_y = 1

    for value in route:
        # print(value, N)
        if(value == 'L' and check(init_y - 1, N)):
            init_y = init_y - 1
            #init_y = init_y + 0
        if(value == 'R' and check(init_y + 1, N)):
            init_y = init_y + 1
        if(value == 'U' and check(init_x - 1, N)):
            init_x = init_x - 1
        if(value == 'D' and check(init_x + 1, N)):
            init_x = init_x + 1    

    print(init_x, init_y)    

if __name__ ==  "__main__":
    main()    
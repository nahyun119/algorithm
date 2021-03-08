# 통과하긴했는데, 시간이 너무 오래걸린다..

def check(string):
    for i in range(len(string) // 2):
        if string[i] != string[-i-1]:
            return False 
    return True
    

def solve():
    words = []
    for i in range(100):
        temp = list(input().strip())
        words.append(temp)
    
    for i in range(100, -1, -1):
        for x in range(100):
            is_done = False 
            for y in range(100):
                if y + i - 1 >= 100:
                    is_done = True 
                    break     
                if y + i - 1 < 100: # row 범위가 가능하다면 
                    row = words[x][y: i + y]
                    if check(row):
                        return i
                if x + i - 1 < 100: # col 범위가 가능하다면 
                    col = [words[k][y] for k in range(x, i + x)]
                    if check(col):
                        return i

            if x + i - 1 >= 100:
                break 

            if is_done:
                continue
                    


def main():
    #T = int(input())
    for i in range(1):
        n = int(input())
        result = solve()
        print("#" + str(n), result)

if __name__ ==  "__main__":
    main()

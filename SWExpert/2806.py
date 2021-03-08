# 대각선 처리하는 방법을 이해를 모샣서 애를 먹었다.. 
# abs 이용해서 값이 같으면 대각선 위에 있다는 것으로 진행 ~

from collections import deque
import copy
def solve():
    n = int(input())
    
    start = [(0, x) for x in range(n)]

    def check(x, y):
        q = deque()
        q.append((x, y, [y]))

        count = 0
        result = []
        while q:
            cx, cy, col = q.popleft()
            #print(cx, cy, col)
            if len(col) >= n:
                count  += 1
                result.append(col)
                continue

            avail = []
            
            for i in range(n):
                nx = cx + 1
                ny = i 


                is_ok = True
                for j in range(cx + 1):
                    if abs(j - nx) == abs(col[j] - ny): # 대각선에 있으면 
                        is_ok = False 

                if i in col:
                    is_ok = False # 이미 퀸이 있는 행이라면 

                if is_ok:
                    c = copy.deepcopy(col)
                    c.append(ny)
                    q.append((nx, ny, c))


        #print(result)
        return count

    total = 0
    for s in start:
        value = check(s[0], s[1])    
        total += value 
    
    return total



def main():
    T = int(input())
    for i in range(T):
        result = solve()
        print("#" + str(i + 1), result)

if __name__ ==  "__main__":
    main()
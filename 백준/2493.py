# 시간초과 발생 
# stack을 활용해보자 

import sys
input = sys.stdin.readline

def main():
    n = int(input())
    tower = list(map(int, input().split()))

    stack = []

    #print(stack)
    result = [0] * n 

    for i in range(n):
        #print(tower[i], stack)
        while stack:
            if stack[-1][0] > tower[i]: # ex) 9, 5 처럼 
                result[i] = stack[-1][1] + 1
                break 
            stack.pop() # 하나씩 뺀다. 
        
        stack.append((tower[i], i)) # 하나씩 탐색했으므로 


        
    print(*result)
                


if __name__ ==  "__main__":
    main()
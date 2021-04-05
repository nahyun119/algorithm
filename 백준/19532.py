import sys 
input = sys.stdin.readline 
a,b,c,d,e,f = map(int, input().split())


for x in range(-999, 1000):
    for y in range(-999, 1000):
        num1 = a * x + b * y 
        num2 = d * x + e * y 
        if num1 == c and num2 == f:
            print(x, y)
            exit()
        
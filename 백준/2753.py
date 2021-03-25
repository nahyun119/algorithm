n = int(input())
flag1 = False 
flag2 = False 
if n % 4 == 0 and n % 100 != 0: # 4의 배수이면서 100의 배수가 아닌경우 
    flag1 = True 
if n % 400 == 0: # 400의 배수인 경우 
    flag2 = True 

if flag1 or flag2:
    print(1)
else:
    print(0)


import sys 
input = sys.stdin.readline 

def test(string):
    flag1 = False # 모음을 반드시 한 개 이상 포함
    flag2 = True # 모음 3개 연속 또는 자음 3개 연속 
    flag3 = True # 같은 문자 연속 2개 이상 안됨. ee, oo 제외 

    list_a = ['a', 'e', 'i', 'o' , 'u']
    pre = string[0] # 맨처음문자
    count = 1 # 자음, 모음 연속 확인 
    if pre in list_a:
        flag1 = True # 맨 처음 문자에 대해서 확인


    for s in string[1:]:
        # print(pre, s)
        if s in list_a: # 모음인 경우 
            flag1 = True 
            if pre in list_a: # 이전 문자도 모음인 경우 
                # print("모음 모음")
                count += 1 
                if count >= 3:
                    flag2 = False # 모음이 3개 연속인 경우 
                    break 
            else: # 이전 문자가 자음인 경우 
                # print("모음 자음")
                count = 1
        else: # 자음인 경우 
            if pre in list_a: # 이전 문자가 모음인 경우 
                # print("자음 모음")
                count = 1 
            else: # 이전 문자가 자음인 경우 
                # print("자음 자음")
                count += 1
                if count >= 3: # 자음이 연속 3개인 경우 
                    flag2 = False 
                    break 
        
        if s == pre and s not in ('e', 'o'): # 같은 문자인 경우 
            flag3 = False 
            break 
        pre = s # 이전 문자 업데이트

    # print(flag1, flag2, flag3)

    if not flag1 or not flag2 or not flag3:
        print('<' + string + '> is not acceptable.')
    else:
        print('<' + string + '> is acceptable.')

while True:
    temp = input().strip()
    if temp == 'end':
        break 
    else:
        test(temp)
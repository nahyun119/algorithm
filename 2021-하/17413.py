import sys 
input = sys.stdin.readline 

string = input().strip()
answer = ''

flag = False # tag안에 데이터인 경우 
temp = '' #단어 담는

for s in string:
    if not flag: # tag가 아닌 경우 
        if s == '<': #tag가 아닌 경우 
            # tag 시작전 앞에 단어가 있는 경우 
            if temp != '':
                answer += temp[::-1]
                temp = ''
            answer += s 
            flag = True 
        else:
            if s == ' ': # 공백인 경우 단어 ~
                answer += temp[::-1] # 문자열 뒤집은거 
                answer += s
                temp = '' # 초기화  
            else: # 공백이 아닌 경우 
                temp += s 

    else: # tag인 경우 
        if s == '>' : # tag 종료 
            answer += s 
            flag = False 
        else: # 문자인 경우 
            answer += s 
    # print(s, flag, temp, answer)

if temp != '':
    answer += temp[::-1]

print(answer)
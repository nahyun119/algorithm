import sys 
input = sys.stdin.readline 

n = int(input())

## 길이가 3 ~ 100,000이므로 모든 경우에 대해서 진행할 필요가 없다.
# 회문을 돌리면서 문자가 다른 경우에 다른 문자를 각각 뺀 문자열에 대해서 다시한번 회문을 돌린다.
# 여기서 회문이 되면 유사회문이 되는 것이고, 아니라면 회문이 되지 않는 것이다. -> 문자를 한번만 빼니까!


def test(string, count): # 회문인지 아닌지 판단하는 함수 
    flag = True  # 회문
    flag2 = True  # 유사회문 
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]: # 앞뒤 방향이 다른 경우 
            flag = False 
            if count == 0: # 제거한 문자 수 
                ans1 = test(string[: i] + string[i + 1:], 1)
                index = len(string) - abs(-i - 1)
                ans2 = test(string[:index] + string[index + 1:], 1) # 각 문자에 대해서 제거한 후 회문인지 아닌지 확인
                # print(string[: i] + string[i + 1:], string[:index] + string[index + 1:])
                if ans1 == 0 or ans2 == 0: # 
                    return 1 # 유사회문
            return 2
    return 0

for i in range(n):
    s = input().strip()
    print(test(s, 0))

    
 

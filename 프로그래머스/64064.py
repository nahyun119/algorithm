import itertools 

def check(banned_id, per):
    for i in range(len(banned_id)):
        #print(banned_id[i], per[i])
        if len(banned_id[i]) == len(per[i]):
            for j in range(len(banned_id[i])):
                if banned_id[i][j] != '*' and banned_id[i][j] != per[i][j]:
                    return False
        else:
            return False
    return True

def solution(user_id, banned_id):
    answer = 0
    
    ans = []
    for per in itertools.permutations(user_id, len(banned_id)):
        result = check(banned_id, per)
        if check(banned_id, per):
            s_per = set(per)
            #print(s_per)
            if s_per not in ans:
                ans.append(s_per)
    
    answer = len(ans)
    
    return answer
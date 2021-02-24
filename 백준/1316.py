import sys
input = sys.stdin.readline

def main():
    n = int(input())

    words = []
    for _ in range(n):
        words.append(input().strip())
    
    count = 0
    for word in words:
        list_word = list(word)
        temp = set(list_word)
        hash_map = {}
        is_group = True
        for t in temp:
            hash_map[t] = 0
        
        for i, w in enumerate(list_word):
            if hash_map[w] == 0: # 한번도 안나온 단어라면
                hash_map[w] = 1
            elif hash_map[w] == 1 and list_word[i - 1] == w: # 나왔지만 이전 단어랑 동일하다면
                hash_map[w] = 1
            else: # 그렇지 않으면 그룹 단어가 아니다 
                is_group = False

        if is_group:
            count += 1

    print(count)


        

if __name__ ==  "__main__":
    main()
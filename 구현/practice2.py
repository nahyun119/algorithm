def main():
    S = str(input())

    list_s = list(S)
    list_s.sort()

    sum = 0
    result = ""

    for value in list_s:
        if ord(value) < ord('A'): # 알파벳이 아닌 숫자인 경우, 0이 48, A가 65, a가 97
            sum += int(value)
        else: # 알파벳인 경우 
            result += value

    result += str(sum)        
    print(result)

if __name__ ==  "__main__":
    main()  
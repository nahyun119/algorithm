def main():
    n = int(input())
    
    for i in range(1, n + 1):
        value = ''
        l_num = list(str(i))
        if '3' in l_num:
            c = l_num.count('3')
            value += '-' * c
        if '6' in l_num:
            c = l_num.count('6')
            value += '-' * c
        if '9' in l_num:
            c = l_num.count('9')
            value += '-' * c
        if '3' not in l_num and '6' not in l_num and '9' not in l_num:
            value = i
        print(value, end = ' ')
    

if __name__ ==  "__main__":
    main()
for t in range(10):
    n, password = map(str, input().split())
    n = int(n)
    l_password = list(password)
    
    while True:
        position = set()
        for i in range(len(l_password) - 1):
            if l_password[i] == l_password[i + 1]:
                if i not in position:
                    position.add(i)
                    position.add(i + 1)

        if not position:
            break 
        temp = []
        for i in range(len(l_password)):
            if i not in position:
                temp.append(l_password[i])
        #print(temp, position)
        l_password = temp
    
    print("#" + str(t + 1), "".join(l_password))
    #print(l_password)

        
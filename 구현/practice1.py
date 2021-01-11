def main():
    N = int(input())

    list_n = str(N)
    
    left_sum = 0
    right_sum = 0

    for index in range(len(list_n)):
        if index < (len(list_n) // 2):
            left_sum += int(list_n[index])
        else:
            right_sum += int(list_n[index])
            
    if left_sum == right_sum:
        print("LUCKY")
    else:
        print("READY")
    

if __name__ ==  "__main__":
    main()   
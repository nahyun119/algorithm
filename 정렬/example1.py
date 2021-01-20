def main():
    N = int(input())

    num_list = []
    for value in range(N):
        num_list.append(int(input()))

    num_list.sort()
    num_list.reverse()

    ## sorted 를 이용한 방법
    # num_list = sorted(num_list, reverse = True)

    for value in num_list:
        print(value, end = ' ')
    #print(num_list)

if __name__ ==  "__main__":
    main() 
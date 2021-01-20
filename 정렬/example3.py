def main():
    # A 정렬을 오름차순 정렬
    # B 정렬을 내림차순 정렬

    N, K = map(int, input().split())


    a = list(map(int, input().split()))
    b =  list(map(int, input().split()))

    a.sort()
    b = sorted(b, reverse = True)

    #print(a, b)
    for i in range(K):
        if a[i] < b[i]: # b의 원소가 큰 경우 변경 
            a[i], b[i] = b[i], a[i]
        else: # 크거나 반복문 탈출 최대 k번 변경하는 것이므로 
            break

    print(sum(a))

if __name__ ==  "__main__":
    main() 
def sequential_search(array, target, N):
    for i in range(N):
        if array[i] == target:
            return i + 1 # 문자열 위치 반환 인덱스는 0부터 시작이므로 + 1

def main():
    print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
    input_data = input().split()

    N = int(input_data[0])
    target = input_data[1]

    print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
    array = list(map(str, input().split()))

    print(sequential_search(array, target, N))


if __name__ ==  "__main__":
    main()                           
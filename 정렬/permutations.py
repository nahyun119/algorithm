import itertools 
numbers = list(map(int, input().split()))
n = len(numbers)
k = int(input())

print(list(itertools.permutations(numbers, k)))


print("===================")
def permutations(arr, depth, n, k):
    if depth == k:
        print(arr[:k])
        return 
    
    for i in range(depth, n, 1):
        arr[i], arr[depth] = arr[depth], arr[i] # 변경 
        permutations(arr, depth + 1, n, k)
        arr[i], arr[depth] = arr[depth], arr[i] # 변경하고 다시 돌아옴 

permutations(numbers, 0, n, k)
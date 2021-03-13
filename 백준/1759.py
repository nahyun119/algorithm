import sys
import itertools
input = sys.stdin.readline
l, c = map(int, input().split())
alphabets = list(map(str, input().split()))

need = ['a', 'e', 'i', 'o', 'u']

#print(alphabets)

alphabets.sort()

avail = list(itertools.combinations(alphabets, l))

for i in range(len(avail)):
    count = 0
    for j in range(5):
        if need[j] in avail[i]: # 최소 한 개 이상의 자음 
            #print("".join(avail[i]))
            count += 1
    if l - 2 >= count and count > 0: # 최소 2개의 자음 & 최소 1개의 모음
        print("".join(avail[i]))

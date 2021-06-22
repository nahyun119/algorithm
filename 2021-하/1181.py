import sys 
input = sys.stdin.readline 

n = int(input())
l_string = set([])
for i in range(n):
    l_string.add(input().strip())

l_string = list(l_string)
l_string.sort(key = lambda x : (len(x), x))


# 중복되는 단어는 한번만 보여줄 수 있도록 한다. 
# print(l_string)
for i in l_string:
    print(i)
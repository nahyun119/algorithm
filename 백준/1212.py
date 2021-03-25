import sys 
input = sys.stdin.readline
n = input().strip()
n = '0o' + n
result = int(n, 8)

print(str(bin(result))[2:])

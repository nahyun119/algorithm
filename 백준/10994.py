import sys
input = sys.stdin.readline

n = int(input())
m = (n - 1) * 4 + 1

for i in range(1, n):
    number = (n - i) * 4 + 1
    print((i - 1) * '* ' + number * '*' + (i - 1) * ' *')
    print(i * '* ' + (number - 4) * ' ' + i * ' *')
print((n - 1) * '* ' + '*' + ' *' * (n - 1))
for i in range(n - 1, 0, -1):
    number = (n - i) * 4 + 1
    print(i * '* ' + (number - 4) * ' ' + i * ' *')
    print((i - 1) * '* ' + number * '*' + (i - 1) * ' *')





    
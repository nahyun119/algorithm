import sys
input = sys.stdin.readline

original = input().strip()
bomb = input().strip()

while original.find(bomb) != -1:
    original = original.replace(bomb, "")

if not original:
    print("FRULA")
else:
    print(original)
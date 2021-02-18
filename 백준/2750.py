import sys
input = sys.stdin.readline

def main():
    n = int(input())
    numbers = []

    for _ in range(n):
        numbers.append(int(input()))
    
    numbers.sort()
    
    for number in numbers:
        print(number)

if __name__ ==  "__main__":
    main()
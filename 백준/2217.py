import sys
input = sys.stdin.readline

def main():
    n = int(input())
    weights = []
    for _ in range(n):
        weights.append(int(input()))
    
    min_value = min(weights)
   
        

if __name__ ==  "__main__":
    main()
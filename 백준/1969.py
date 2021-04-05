import sys 
import itertools 
input = sys.stdin.readline 
n, m = map(int, input().split())
dna = []

new = ['A', 'C', 'G', 'T']

for i in range(n):
    dna.append(input().strip())

result = ''
result_value = 0

for i in range(m):
    dna_count = [0] * 4 
    for j in range(n):
        if dna[j][i] == 'A':
            dna_count[0] += 1
        elif dna[j][i] == 'C':
            dna_count[1] += 1
        elif dna[j][i] == 'G':
            dna_count[2] += 1
        elif dna[j][i] == 'T':
            dna_count[3] += 1
    count = max(dna_count)
    for i in range(4):
        if count == dna_count[i]:
            result += new[i]
            result_value += (n - count)
            break 
# print("-=========")
print(result)
print(result_value)
    

        
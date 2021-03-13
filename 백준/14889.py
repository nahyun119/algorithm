import itertools 
import sys 
input = sys.stdin.readline

n = int(input())

scores = []
for i in range(n):
    scores.append(list(map(int, input().split())))

people = [x for x in range(n)]

comb = list(itertools.combinations(people, n // 2))
min_value = 1e9
for i in range(len(comb) // 2):
    a = 0
    team1 = comb[i]
    for x in range(n // 2):
        for y in range(x + 1, n // 2):
            a += scores[team1[x]][team1[y]] + scores[team1[y]][team1[x]]
    b = 0
    team2 = comb[-i-1] # combinations 결과를 보면 comb[i]랑 comb[-i-1] 이랑 완전히 다른걸 알 수 있다. 
    for x in range(n // 2):
        for y in range(x + 1, n // 2):
            b += scores[team2[x]][team2[y]] + scores[team2[y]][team2[x]]
    min_value = min(min_value, abs(a - b))

print(min_value)


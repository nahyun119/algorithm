import itertools
n = int(input())
k = int(input())
cards = []
for i in range(n):
    cards.append(str(input()))

temp = set(map(lambda x : ''.join(x), itertools.permutations(cards, k)))
# temp = list(itertools.permutations(cards, k))
print(len(temp))
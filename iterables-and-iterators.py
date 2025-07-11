from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

comb = list(combinations(letters, k))
count = sum(1 for c in comb if 'a' in c)

print(f"{count/len(comb):.4f}")

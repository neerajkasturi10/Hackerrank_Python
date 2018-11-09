from itertools import combinations_with_replacement
A, k = input().split()
comb = combinations_with_replacement(sorted(A), r = int(k))
for x in comb:
    print(''.join(x))
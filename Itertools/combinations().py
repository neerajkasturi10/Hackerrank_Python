from itertools import combinations
A, k = input().split()
for i in range(1,(int(k)+1)):
    comb = combinations(sorted(A),i)
    for x in comb:
        print(''.join(x))
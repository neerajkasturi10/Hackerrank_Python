from itertools import permutations
A, k = input().split()
P = sorted(permutations(A,r = int(k)))
for x in P:
    print (''.join(x))
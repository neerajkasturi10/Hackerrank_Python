from collections import defaultdict
n, m = map(int, input().split())
A = defaultdict(list)
B = []
for i in range(n):
    A[input()].append(i+1)
for _ in range(m):
    B.append(input())
#output = defaultdict(int)

for x in B:
    if(x in A.keys()):
        print(*A[x])
    else:
        print('-1')
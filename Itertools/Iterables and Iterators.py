import itertools
n = int(input())
num = list(input().split())
k = int(input())

def fact(x):
    if( x == 0):
        return 1
    else:
        return x * fact(x-1)

comb_len = (fact(n))/((fact(n-k)*fact(k)))

comb = itertools.combinations(sorted(num),k)
count = 0
for x in comb:
    if ('a' in x):
        count+=1
    else:
        continue

print (count/comb_len)
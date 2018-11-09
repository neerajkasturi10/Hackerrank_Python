from itertools import product

A = list(map(int,input().split()))
B = list(map(int,input().split()))

prod = product(A,B)
for each in prod:
    print(each, end = " ")
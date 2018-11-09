import re
n = int(input())
fl = "[+-]?[0-9]*[.][0-9]+"
for _ in range(n):
    s = input()
    print (bool(re.fullmatch(fl,s)))
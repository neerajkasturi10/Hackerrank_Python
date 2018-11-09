import re
t = int(input())
for i in range(t):
    try:
        reg_exp = re.compile(input())
        print("True")
    except re.error:
        print("False")
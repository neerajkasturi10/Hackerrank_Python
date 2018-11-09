import re
regex = input().strip()
reg_exp = r"([0-9a-zA-Z])\1+"

if(re.search(reg_exp,regex)):
    m = re.findall(reg_exp,regex)
    print(m[0])
else:
    print('-1')


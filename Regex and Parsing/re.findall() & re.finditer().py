import re
v = "aeiou"
con = "qwrtypsdfghjklzxcvbnm"

reg_exp = r'(?<=['+con+'])(['+v+']{2,})(?=['+con+'])'

sub_vowel = re.findall(reg_exp,input().strip(),flags = re.I)
print ('\n'.join(sub_vowel or ["-1"]))
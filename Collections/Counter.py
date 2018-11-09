from collections import Counter

X = int(input())
myList = list(map(int, input().split()))
counter_list = Counter(myList)
N = int(input())
money = 0
for _ in range(N):
    ss, x = map(int, input().split())
    if (ss in counter_list.keys()):
        if (counter_list[ss] >= 1):
            money += x
            counter_list[ss] -= 1
        else:
            counter_list.pop(ss, None)
    else:
        continue

print(money)
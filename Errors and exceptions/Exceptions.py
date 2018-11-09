n = int(input())
for i in range(n):
    try:
        inp = input().split()
        a = inp[0]
        b = inp[1]
        print (int(a)//int(b))
    except Exception as e:
        print ("Error Code:", e)
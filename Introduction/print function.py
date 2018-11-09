if __name__ == '__main__':
    n = int(input())
    if (n == 1):
        print ('1')
    else:
        a = str(1)
        for i in range(2,n+1):
            a = a + str(i)
        print (a)
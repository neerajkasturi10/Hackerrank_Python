cube = lambda x: pow(x,3)# complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    a = 0
    b = 1
    fib = []
    if (n == 0):
        return fib
    elif (n == 1):
        fib.append(a)
        return fib
    elif (n == 2):
        fib.extend([a,b])
        return fib
    else:
        fib.extend([a,b])
        for i in range(2,n):
            fib.append(a+b)
            a,b = fib[i-1],fib[i]
        return fib
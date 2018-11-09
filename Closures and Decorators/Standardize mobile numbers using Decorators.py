def wrapper(f):
    def fun(l):
        # complete the function
        for num in range(len(l)):
            l[num] = '+91'+' '+l[num][-10:-5]+' '+l[num][-5:]
        return f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
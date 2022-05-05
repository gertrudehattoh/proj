def fib(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    elif x<0:
        return 0
    else:
        return fib(x) + fib(x-1)

def fib(n):
    a,b=0,1

    for i in range(n):
        tmp=a+b
        a=b
        b=tmp
    return a



print(fib(5))
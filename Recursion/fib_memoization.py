f =[-1]*10
def fib_memo(n):
    if n<=1:
        f[n] = n
        return n
    else:
        if f[n-2]==-1:
            f[n-2]=fib_memo(n-2)
        elif f[n-1]==-1:
            f[n-1]=fib_memo(n-1)
    return fib_memo(n-2)+fib_memo(n-1)

print(fib_memo(7))
def tay_loop(m,n):
    sum = 1
    p = 1
    f = 1
    for i in range(1,n+1):

        p *= m
        f *= i
        sum += p / f
    return sum

print(tay_loop(1,10))

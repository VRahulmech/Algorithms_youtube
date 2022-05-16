def fun1(n):

    while n>0:
        print(n)
        return fun1(n-1)

fun1(6)
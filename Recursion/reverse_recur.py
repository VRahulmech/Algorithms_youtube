def fun2(n):
    while n>0:
        fun2(n-1)
        print(n)
        return
fun2(6)
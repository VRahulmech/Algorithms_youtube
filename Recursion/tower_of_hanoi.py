def toh(n,a,b,c):
    if n>0:
        toh(n-1,a,c,b)
        print(a,'to',c)
        toh(n-1,b,a,c)
    return

print(toh(4,1,2,3))
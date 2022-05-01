def gcd(a,b):
    if a>b:
        a,b = b,a

    if b%a==0:
        return a
    else:
        return gcd(a,b%a)


print(gcd(2,3))
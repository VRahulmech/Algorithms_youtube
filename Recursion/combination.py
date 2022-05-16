def ncr(n,r):
    if n==r:
        return 1
    elif r==0:
        return 1
    return ncr(n-1,r-1)+ncr(n-1,r)

print(ncr(3,2))